from django.contrib import admin
from django.db.models import Count
from . import models


class CollegeAdmin(admin.ModelAdmin):
    list_display = ["__str__", "student_count", "lecturer_count"]
    

    def student_count(self, college):
        return college.student_count
    
    def lecturer_count(self, college):
        return college.lecturer_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count = Count("department__program__student", distinct=True),
            lecturer_count = Count("department__lecturer", distinct=True)
        )



class StudentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "reg_no"]
    list_select_related = ["user"]






admin.site.register(models.College, CollegeAdmin)
# admin.site.register(models.Course)
admin.site.register(models.Department)
admin.site.register(models.Lecturer)
admin.site.register(models.Program)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Organization)
admin.site.register(models.Staff)

