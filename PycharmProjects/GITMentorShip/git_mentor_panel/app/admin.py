from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# admin.site.register(CustomUser)


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


# Register your models here.
admin.site.register(CustomUser, UserModel)
