from django.contrib import admin
from webprofile.models import UserProfile
from company.models import Company,TestModel
from sites.models import ForgotPassword


# Register your models here.

admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(TestModel)
admin.site.register(ForgotPassword)
