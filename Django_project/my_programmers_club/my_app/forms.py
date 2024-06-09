from django import forms
from .models import Member

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            "firstname",
            "lastname",
            "phone",
            "age",
            "married",
            "joined_date",
            "user_image",
        )

        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "married": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "joined_date": forms.DateInput(attrs={"class": "form-control"}),
            "user_image": forms.FileInput(attrs={"class": "form-control"}),
        }


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap classes to the password fields if they haven't been applied
        for field_name in ["password1", "password2"]:
            if "class" in self.fields[field_name].widget.attrs:
                self.fields[field_name].widget.attrs["class"] += " form-control"
            else:
                self.fields[field_name].widget.attrs["class"] = "form-control"


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
