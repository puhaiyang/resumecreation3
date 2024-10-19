# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Resume, Template, User
from .serializers import ResumeSerializer, TemplateSerializer, UserWithDataSerializer


# user api
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    if User.objects.filter(username=data.get('username')).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=data.get('username'), email=data.get('email'),
                                    password=data.get('password'))
    user.is_admin = data.get('is_admin', False)
    user.save()
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


# login
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            data.update({
                'username': request.data.get('username'),
            })
            return Response(data)
        return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_admin': user.is_admin
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout_user(request):
    try:
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# resume api
@api_view(['POST'])
def create_resume(request):
    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_resumes(request):
    resumes = Resume.objects.filter(user=request.user)
    serializer = ResumeSerializer(resumes, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_resume(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id, user=request.user)
    except Resume.DoesNotExist:
        return Response({'error': 'Resume not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ResumeSerializer(resume, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_resume(request, resume_id):
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_user(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id, user=request.user)
        resume.delete()
        return Response({'message': 'Resume deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Resume.DoesNotExist:
        return Response({'error': 'Resume not found'}, status=status.HTTP_404_NOT_FOUND)


# template api
@api_view(['GET'])
def get_all_templates(request):
    templates = Template.objects.all()
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_template_details(request, template_id):
    try:
        template = Template.objects.get(id=template_id)
        serializer = TemplateSerializer(template)
        return Response(serializer.data)
    except Template.DoesNotExist:
        return Response({'error': 'Template not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_templates(request, template_id):
    try:
        template = Template.objects.get(template_id=template_id)
        Resume.objects.filter(template_id=template).delete()
        # 删除模板
        template.delete()
        # 删除用户
        template.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Template.DoesNotExist:
        return Response({"detail": "Template not found."}, status=status.HTTP_404_NOT_FOUND)


# admin - user management api
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserWithDataSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
