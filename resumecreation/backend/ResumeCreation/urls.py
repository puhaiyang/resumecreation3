"""
URL configuration for ResumeCreation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CVBuilder.views import register_user, CustomTokenObtainPairView, check_auth, logout_user, create_resume, \
    get_all_resumes, update_resume, delete_resume, get_all_templates, get_template_details, get_all_users, delete_user, \
    delete_templates

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # user managements
    path('api/register/', register_user, name='register_user'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/check-auth/', check_auth, name='check_auth'),
    path('api/logout/', logout_user, name='logout_user'),

    # resume managements
    path('api/resumes/create/', create_resume, name='create_resume'),
    path('api/resumes/', get_all_resumes, name='get_all_resumes'),
    path('api/resumes/<int:resume_id>/', update_resume, name='update_resume'),
    path('api/resumes/<int:resume_id>/', delete_resume, name='delete_resume'),

    # template managements
    path('api/templates/', get_all_templates, name='get_all_templates'),
    path('api/templates/<int:template_id>/', get_template_details, name='get_template_details'),
    path('api/templates/<int:template_id>/delete', delete_templates, name='delete_templates'),

    # admin managements
    path('api/admin/users/', get_all_users, name='get_all_users'),
    path('api/admin/users/<int:id>/', delete_user, name='delete_user'),
]
