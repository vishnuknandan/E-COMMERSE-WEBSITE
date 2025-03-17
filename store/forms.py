from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class userregisterform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        widgets={
                  "username":forms.TextInput(attrs={"class":"form-control"}),
                  "first_name":forms.TextInput(attrs={"class":"form-control"}),
                  "last_name":forms.TextInput(attrs={"class":"form-control"}),
                  "email":forms.EmailInput(attrs={"class":"form-control"}),
                  "password1":forms.PasswordInput(attrs={"class":"form-control"}),
                  "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }

class userloginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))


class userorderform(forms.Form):
    address = forms.CharField(widget=forms.Textarea, required=True)


   
        