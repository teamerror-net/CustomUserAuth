## Custom User Authentacation

This repository refers Django custom user authentacation system.

### Create Project - 

#### Run bellow command on your command prompt


    python manage.py startproject CustomUserAuth


### Create Apps - 

#### Run bellow command on your command prompt

    python manage.py startapp account


#### Go to your project settings.py file and add 'account' on install apps section.


INSTALLED_APPS = [

    'account',
]

#### Go to account/models.py and import bellow module.

    from django.db import models
    from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
    from django.utils import timezone
    from account.manager import UserManager
    
#### Create CustomUserModel

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
            
