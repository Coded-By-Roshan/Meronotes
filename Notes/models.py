from django.db import models
from django.contrib.auth.models import User
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Note(models.Model):
    title = models.CharField(default='', max_length=10000, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='meronotes',storage=gd_storage)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Feeds(models.Model):
    full_name = models.CharField(max_length=500, default='')
    experience = models.TextField(max_length=9999999999)

    def __str__(self):
        return f"Feedback from {self.full_name}"