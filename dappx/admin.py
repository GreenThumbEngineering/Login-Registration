from django.contrib import admin

# Register your models here.
# dappx/admin.py
from dappx.models import UserProfileInfo, User
admin.site.register(UserProfileInfo)