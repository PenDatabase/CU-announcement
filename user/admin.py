from django.contrib import admin
from . import models


admin.site.register(models.College)
admin.site.register(models.Course)
admin.site.register(models.Department)
admin.site.register(models.Lecturer)
admin.site.register(models.Program)
admin.site.register(models.Student)
admin.site.register(models.Organization)
admin.site.register(models.Staff)

