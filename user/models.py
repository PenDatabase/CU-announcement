from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re



# Model for Colleges
class College(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



# Model for Departments
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=15, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super().save(*args, **kwargs)




# Model for Programs
class Program(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name




# Model for Courses
# class Course(models.Model):
#     title = models.CharField(max_length=255)
#     code = models.CharField(max_length=8, unique=True)
#     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return f"{self.code} - {self.title}"



# Model for Lecturers
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    validated = models.BooleanField(default=False)

    def college(self):
        return self.department.college

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return f"@{self.user}"




# Model for Students
class Student(models.Model):
    LEVELS = [
        (100, "100 Level"),
        (200, "200 Level"),
        (300, "300 Level"),
        (400, "400 Level"),
        (500, "500 Level"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_no = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(r"^\d{2}[a-zA-Z]{2}\d{6}$", "Invalid Matric No.")
        ]
    )
    reg_no = models.CharField(
        max_length=7,
        validators=[RegexValidator(r"^\d{7}$", "Invalid Reg No.")]
    )
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(choices=LEVELS)

    def college(self):
        return self.program.department.college
    
    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return f"{self.reg_no}"
    





# Model for Staff
class Staff(models.Model):
    OFFICES = [
        ("DSA", "Dean of Student Affairs"),
        ("VC", "Vice Chancellor"),
        ("DEPUTY VC", "Deputy Vice Chancellor"),
        ("REGISTRAR", "Registrar"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField(max_length=255, unique=True, choices=OFFICES)

    def clean(self):
        super().clean()

        # making sure email is valid
        if self.user and self.user.email:
            email_pattern = r"^\w+(-\w+)*@covenantuniversity\.edu\.ng$"
            if not re.match(email_pattern, self.user.email):
                raise ValidationError({"user.email": "Invalid CU staff email."})

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.office})"

    class Meta:
        verbose_name_plural = "Staff"


# Model for Organizations
class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
