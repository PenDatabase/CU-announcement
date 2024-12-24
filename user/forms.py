from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models



class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]



class LecturerForm(forms.ModelForm):
    class Meta:
        model = models.Lecturer
        fields = ["department"]



class StudentUserForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ["matric_no", "program", "level"]