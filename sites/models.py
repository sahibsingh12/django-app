from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ForgotPassword(models.Model):

    user = models.ForeignKey(User)
    token = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'forgot_password'