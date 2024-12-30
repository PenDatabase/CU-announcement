from django.contrib import admin
from .models import Announcement,Comment

# Register your models here.



class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["__str__", "announcer", "post_time"]
    exclude = ["post_time"]
    list_filter = ["category"]
    search_fields = ["title", "announcer", "content"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "post_time", "user"]


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Comment, CommentAdmin)


