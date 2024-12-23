from django.db import models
from django.contrib.auth.models import User


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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def college(self):
        return self.department.college




class Student(models.Model):
    LEVELS = {
        "100": "100 Level",
        "200": "200 Level",
        "300": "300 Level",
        "400": "400 Level",
        "500": "500 Level",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(choices=LEVELS)

    def college(self):
        return self.program.department.college
