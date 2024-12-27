from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from . import models
import re



class LecturerUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    # Making sure email matches default lecturer email in CU
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_pattern = r"^[a-z]+(-[a-z]+)*\.[a-z-]+(-[a-z]+)*@covenantuniversity\.edu\.ng$"

        if not re.match(email_pattern, email):
            raise ValidationError("Invalid CU lecturer email.")
        return email




class StudentUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    # Making sure email matches default student email in CU
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_pattern = r"^[a-z]+(-[a-z]+)*\.\d{7}@stu\.cu\.edu\.ng$"

        if not re.match(email_pattern, email):
            raise ValidationError("Invalid CU student email.")
        return email




class LecturerCreationForm(forms.ModelForm):
    class Meta:
        model = models.Lecturer
        fields = ["department"]



class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ["matric_no", "reg_no", "program", "level"]
    
    def clean_matric_no(self):
        # Matric no is required for students in all levels except 100 level
        matric_no = self.cleaned_data.get("matric_no")
        level = self.cleaned_data.get("level")

        if level != 100 and not matric_no:
            raise ValidationError("Matric No. required for levels other than 100.")