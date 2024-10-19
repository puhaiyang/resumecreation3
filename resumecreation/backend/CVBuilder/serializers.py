from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Resume, Template


# 自定义的通过email和密码校验的认证器
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # 获取 email 和 password
        email = attrs.get("username")
        password = attrs.get("password")

        # 使用 email 找到对应的用户
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # 进行身份验证
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        # 调用父类的验证逻辑（返回 token）
        data = super().validate(attrs)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['resume_id', 'user', 'template_id', 'name', 'content', 'created_time', 'updated_time',
                  'revision_time']


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['template_id', 'user', 'name', 'description', 'content', 'created_time', 'updated_time']


class UserWithDataSerializer(serializers.ModelSerializer):
    resumes = ResumeSerializer(many=True, read_only=True)
    templates = TemplateSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'resumes', 'templates']
