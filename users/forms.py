from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label = 'Username',
        required = True
    )
    password = forms.CharField(
        required = 'True',
        widget = forms.PasswordInput(
            attrs={'class': 'form-group'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username).first()
        if not query:
            self.add_error('username', 'User does not exist')
        


class RegisterForm(forms.Form):

    username = forms.CharField(
        label='Username',
        required=True
    )
    email = forms.EmailField(
        label = 'Email',
        required = True
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group'}
        )
    )
    password2 = forms.CharField(
        label='Confirm your password',
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group'}
        )
    )

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username).first()
        if query:
            self.add_error('username', 'User already exists')
    
    
    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if not (pass1 and pass2 and pass1 == pass2):
            self.add_error('password2', 'Passwords do not match')