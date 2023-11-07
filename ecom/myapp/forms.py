from django import forms
from.models import UserRegistration,UserLogin

class Registration(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"
        widgets = {

        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = "__all__"
        widgets = {

        }