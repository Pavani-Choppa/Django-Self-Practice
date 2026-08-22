from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if " " in username:
            raise forms.ValidationError("UserName cannot Contain Spaces")
        return username


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "login-input",
                "placeholder": "Enter your username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "login-input",
                "placeholder": "Enter your password",
            }
        )
    )