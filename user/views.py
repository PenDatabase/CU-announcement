from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.db import transaction
from . import forms





def lecturer_register(request):

    if request.method == "POST":
        LecturerUserForm = forms.LecturerUserForm(request.POST)
        LecturerCreationForm = forms.LecturerCreationForm(request.POST)

        # Use a transaction to ensure atomicity
        if LecturerUserForm.is_valid() and LecturerCreationForm.is_valid():
            with transaction.atomic():
                # Create Lecturer User
                LecturerUser = LecturerUserForm.save(commit=False)
                LecturerUser.set_password(LecturerUser.password)
                LecturerUser.save()

                # Create Lecturer
                Lecturer = LecturerCreationForm.save(commit=False)
                Lecturer.user = LecturerUser
                Lecturer.save()

                return redirect('login')
        # else:
        #     # Handle form errors (e.g., return to the form with errors displayed)
        #     context = {
        #         'LecturerUserForm': LecturerUserForm,
        #         'LecturerCreationForm': LecturerCreationForm,
        #     }
        #     return render(request, 'register_lecturer.html', context)

    else:
        LecturerUserForm = forms.LecturerUserForm()
        LecturerCreationForm = forms.LecturerCreationForm()

    context = {
        "LecturerUserForm": LecturerUserForm,
        "LecturerCreationForm": LecturerCreationForm
    }            
    return render(request, "registration/lecturer_registration.html", context)




def student_register(request):
    if request.method == "POST":
        StudentUserForm = forms.StudentUserForm(request.POST)
        StudentCreationForm = forms.StudentCreationForm(request.POST)

        if StudentUserForm.is_valid() and StudentCreationForm.is_valid():
            # Create Student User
            StudentUser = StudentUserForm.save(commit=False)
            StudentUser.set_password(StudentUser.password)

            StudentUser.save()

            # Create Student
            Student = StudentCreationForm.save(commit=False)
            Student.user = StudentUser
            Student.save()

            return redirect('login')
        
    else:
        StudentUserForm = forms.StudentUserForm()
        StudentCreationForm = forms.StudentCreationForm()

    context = {
        "StudentUserForm": StudentUserForm,
        "StudentCreationForm": StudentCreationForm
    }            
    return render(request, "registration/student_registration.html", context)