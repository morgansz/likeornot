# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import Picture
# from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class PictureForm(forms.ModelForm):
#     class Meta:
#         model = Picture
#         fields = ['image']