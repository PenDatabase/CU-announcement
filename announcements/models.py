from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User



# Create your models here.
class Announcement(models.Model):
    announcement_categories = [
        ('Academic','Academic'),
        ('Events','Events'),
        ('Lost_Found', 'Lost & Found'),
        ('Others','Others'),    

    ]

    title = models.CharField(max_length=256)
    category = models.CharField(max_length=50 , choices= announcement_categories)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now=True)

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
    
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=1000)
    post_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on {self.announcement.title}"
