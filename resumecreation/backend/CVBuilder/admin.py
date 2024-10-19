from django.contrib import admin
from .models import Resume, User, Template


# Register your models here.
@admin.register(Template)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description', 'content', 'created_time', 'updated_time')
    search_fields = ('name', 'user_username')


# register Resume model
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_time', 'updated_time')
    search_fields = ('name', 'user_username')
    list_filter = ('user', 'created_time')
    actions = ['mark_as_reviewed', 'mark_as_approved']

    def mark_as_reviewed(self, request, quetyset):
        quetyset.update(status='Reviewed')

    mark_as_reviewed.short_description = 'Mark selected resumes as reviewed'

    def mark_as_approved(self, request, queryset):
        queryset.update(status='Approved')

    mark_as_approved.short_description = 'Mark selected resumes as approved'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')
    actions = ['deactivate_user']

    def deactivate_user(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_user.short_description = 'Deactivate selected users'
