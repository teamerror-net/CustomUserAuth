from django.contrib import admin
from account.models import UserAuth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.

class UserAuthAdmin(UserAdmin):
    search_fields = ('username',)
admin.site.register(UserAuth,UserAuthAdmin)
admin.site.unregister(Group)