from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db import transaction
from . import forms
from .utils import email_is_valid




def lecturer_register(request):
    if request.method == "POST":
        LecturerUserForm = forms.UserForm(request.POST)
        LecturerForm = forms.LecturerForm(request.POST)

        if LecturerUserForm.is_valid() and LecturerForm.is_valid():
            with transaction.atomic():
                # Create User
                LecturerUser = LecturerUserForm.save(commit=False)
                LecturerUser.set_password(LecturerUser.password)
                if email_is_valid(LecturerUser.email, "lecturer"):
                    LecturerUser.save()

                     # Create Lecturer
                    Lecturer = LecturerForm.save(commit=False)
                    Lecturer.user = LecturerUser
                    Lecturer.save()

                    # Create or Get group
                    group, created = Group.objects.get_or_create(name="Lecturers")
                    messages.success(request, "Lecturer registration completed successfully")
                    return redirect('login')
                else:
                    messages.info(request, "This is not a valid CU lecturer email")
    else:
        LecturerUserForm = forms.UserForm()
        LecturerForm = forms.LecturerForm()

    context = {
        "LecturerUserForm": LecturerUserForm,
        "LecturerForm": LecturerForm
    }            
    return render(request, "user/lecturer_registration.html", context)




def student_register(request):
    pass