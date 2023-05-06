## Custom User Authentacation

This repository refers Django custom user authentacation system.

### Install Django - 

#### Run bellow command on your command prompt


    pip install django

### Create Project - 

#### Run bellow command on your command prompt


    python manage.py startproject CustomUserAuth .


### Create Apps - 

#### Run bellow command on your command prompt

    python manage.py startapp account


#### Go to your project settings.py file and add 'account' on install apps section.


INSTALLED_APPS = [

    'account',
]

### Create Custom User Manager -

#### Create a new file called manager.py on account folder and import bellow module -

    from django.contrib.auth.base_user import BaseUserManager

#### Create UserManager class on your manager.py file.

    class UserManager(BaseUserManager):
        def create_user(self, username, password, **extra_fields):
            if not username:
                raise ValueError('Users must have a username')
            user = self.model(username = username, **extra_fields)
            user.set_password(password)
            user.save()
            return user

        def create_superuser(self, username, password, **extra_fields):
            user = self.create_user(username, password, **extra_fields)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return user

### Create CustomUserModel -

#### Go to account/models.py and import bellow module.

    from django.db import models
    from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
    from django.utils import timezone
    from account.manager import UserManager #import from account apps
    
#### Create UserAuth class on your models.py file.

    class UserAuth(AbstractBaseUser,PermissionsMixin):
        class Meta:
            verbose_name_plural = "User"
        username = models.CharField(max_length=10,unique=True)
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        email = models.EmailField(max_length=100)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=timezone.now)

        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

        objects = UserManager()

        def __str__(self):
            return self.username
            
### Django Admin -

#### Go to account/admin.py and import bellow module.

    from django.contrib import admin
    from account.models import UserAuth
    from django.contrib.auth.admin import UserAdmin
    from django.contrib.auth.models import Group
    
#### Create UserAuthAdmin class on your admin.py file.

    class UserAuthAdmin(UserAdmin):
        search_fields = ('username',)
    admin.site.register(UserAuth,UserAuthAdmin)
    admin.site.unregister(Group)

### Makemigrate, migration and runserver -

#### Run bellow command to makemigrations

    python manage.py makemigrations
    
#### Run bellow command to migrate

    python manage.py migrate
    
#### Run bellow command to runserver

    python manage.py runserver
    
### Admin access

#### Admin url
    https://127.0.0.1:8000/admin
    
#### Admin username
    admin
    
#### Admin password
    admin

### 📫 How to reach me...

Website: https://teamerror.net

Email: teamerror.net@gmail.com

Linkedin: https://www.linkedin.com/in/mehedi05/

Twitter: https://twitter.com/teamerror_net
