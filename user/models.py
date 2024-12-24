from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class College(models.Model):
    name = models.CharField(max_length=255)



class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=15)
    college = models.ForeignKey(College, on_delete=models.ForeignKey)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
    

    def save(self, *args, **kwargs):
        self.abbreviation = str(self.abbreviation).upper()
        super().save(*args, **kwargs)




class Program(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, models.SET_NULL, null=True)



class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=8, unique=True)
    department = models.ForeignKey(Department, models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.code} - {self.title}"



class Lecturer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField(null=True)
    validated = models.BooleanField(default=False)


    def college(self):
        return self.department.college

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



def validate_reg_no(value):
    if len(str(value)) != 7:
        raise ValidationError("Not a valid registration number")
    


class Student(models.Model):
    LEVELS = {
        "100": "100 Level",
        "200": "200 Level",
        "300": "300 Level",
        "400": "400 Level",
        "500": "500 Level",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=10, validators=[RegexValidator(r"^[0-9]{2}+[a-z]{2}+[0-9]{6}$")])
    reg_no = models.IntegerField(validators=[validate_reg_no])
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(choices=LEVELS)

    def college(self):
        return self.program.department.college

