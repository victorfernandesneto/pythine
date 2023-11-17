from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label = 'Username',
        required = True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Example: pythine_user',
            'class': 'form-control'})
    )
    password = forms.CharField(
        required = 'True',
        widget = forms.PasswordInput(attrs={
            'placeholder': 'Example: imaproductiveperson123',
            'class': 'form-control'
        }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username).first()
        if not query:
            self.add_error('username', 'Wrong credentials for user, try again')
        


class RegisterForm(forms.Form):

    username = forms.CharField(
        label='Username',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Example: pythine_user',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label = 'Email',
        required = True,
        widget = forms.EmailInput(
            attrs={
                'placeholder': "Example: pythine_user@pythine.com",
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username).first()
        if query:
            self.add_error('username', 'User already exists')
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email).first()
        if query:
            self.add_error('email', 'Email already registered')
    
    
    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if not (pass1 and pass2 and pass1 == pass2):
            self.add_error('password2', 'Passwords do not match')