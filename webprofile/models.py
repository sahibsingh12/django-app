from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.ForeignKey(User)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    avatar = models.FileField(default = None , upload_to = 'static/images/')

    class Meta:
        db_table = 'user_profile'