from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from slugify import slugify
# Create your models here.
# from mongoengine import Document,fields

class MyUserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, password=None):
        if not phone:
            return ValueError("Users must have an phone")
        # if not username:
        #     return ValueError("Users must have an username")
        if not first_name or not last_name:
            return ValueError("Users must have a name")
        
        user = self.model(
            # email = self.normalize_email(email),
            # username=username,
            phone = phone,
            first_name = first_name,
            last_name = last_name,
            # is_startup_founder = is_startup_founder
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name, password=None):
        user = self.create_user(
            # email = self.normalize_email(email),
            # username=username,
            phone = phone,
            first_name = first_name,
            last_name = last_name,
            # is_startup_founder=is_startup_founder,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser):
    username = None
    phone = models.CharField(max_length=20,unique=True, primary_key=True)
    # username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # is_startup_founder = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

