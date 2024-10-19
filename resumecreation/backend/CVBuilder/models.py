from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# User model
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Resume model
class Resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='resumes', on_delete=models.CASCADE)
    template_id = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    revision_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} by {self.user.username}"


# Template model
class Template(models.Model):
    template_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='templates', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
