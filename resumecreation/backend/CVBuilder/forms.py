from django import forms
from .models import Resume

#for submitting resume
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'content', 'template_id']

#for verifying login operation
#class LoginForm(forms.Form):
#    username = forms.CharField(max_length = 150, required = True)
#    password = forms.CharField(widget = forms.PasswordInput, required = True)

#for verifying register operation
#class RegisterForm(forms.ModelForm):
#    password = forms.CharField(widget = forms.PasswordInput, required = True)
#
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password']