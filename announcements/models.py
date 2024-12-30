from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from user.models import Lecturer, Staff, Organization



# Create your models here.
class announcements(models.Model):
    announcement_categories = [
        ('Academic','Academic'),
        ('Events','Events'),
        ('Lost_Found', 'Lost & Found'),
        ('Others','Others'),    

    ]

    title = models.CharField(max_length=256)
    categories = models.CharField(max_length=50 , choices= announcement_categories)
    content = models.TextField()
    post_time = models.DateTimeField()

    # Implementing a GenericForeignKey so that the announcer can either be a staff, lecturer or organization
    announcer_type = models.ForeignKey(
                            ContentType,
                            null=True,
                            on_delete=models.SET_NULL,
                            limit_choices_to={
                                    'model__in': ('lecturer', 'staff', 'organization')
                            }
                            )
    announcer_id = models.IntegerField(null=True)
    announcer = GenericForeignKey('announcer_type', 'announcer_id')

    def __str__(self):
        return self.title
    

class comments(models.Model):
    announcement = models.ForeignKey(announcements, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=1000)
    post_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on {self.announcement.title}"
