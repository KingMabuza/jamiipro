from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Exporter


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ExportRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Exporter
        fields = ["Export_Industry","Export_From", "Export_To"]

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["level_of_knowledge","domain_of_Knowledge","type_of_paper"]