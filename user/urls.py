from django.urls import path
from . import views


app_name = "user"


urlpatterns = [
    path("register/lecturer/", views.lecturer_register, name="lecturer_register"),
    path("register/student/", views.student_register, name="student_register"),
]
