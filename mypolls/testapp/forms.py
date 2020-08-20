from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from testapp.models import pollsmodel
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class signupform(UserCreationForm):
    username=forms.CharField(help_text=None)
    password1=forms.CharField(widget=forms.PasswordInput, help_text=None)
    password2=forms.CharField(label="Re-Enter Password",widget=forms.PasswordInput,help_text=None)
    email=forms.CharField(help_text=None)
    class Meta:
        model=User
        fields=['username','password1','password2','email']

# class pollsform(forms.ModelForm):
#     class Meta:
#         model=pollsmodel
#         fields='__all__'

    def clean_email(self):
        inputemail=self.cleaned_data['email']
        if User.objects.filter(email=inputemail).exists():
            raise forms.ValidationError('Email already used')
        return inputemail

class changepasswordform(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput, help_text=None)
    new_password1=forms.CharField(widget=forms.PasswordInput,help_text=None)
    new_password2=forms.CharField(widget=forms.PasswordInput,help_text=None)
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']
