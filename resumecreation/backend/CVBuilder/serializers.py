from rest_framework import serializers

from .models import User, Resume, Template


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['resume_id', 'user', 'template_id', 'name', 'content', 'created_time', 'updated_time', 'revision_time']


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
