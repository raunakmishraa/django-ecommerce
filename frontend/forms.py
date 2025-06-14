# accounts/forms.py
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields # Keeps default fields: username, password, password2

class LoginForm(AuthenticationForm):
    pass

class CustomUserChangeForm(UserChangeForm):
    password = None # Exclude password from the UserChangeForm to prevent direct password change here

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'first_name', 'last_name')
        # You can customize which fields are editable here.
