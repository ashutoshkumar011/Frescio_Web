from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# from .managers import CustomUserManager
# from .managers import UserManager

def CustomUserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, password):
        if not phone:
            raise ValueError('User must enter a contact no.')
        if not first_name:
            raise ValueError('User must enter first name')
        if not last_name:
            raise ValueError('User must enter last name')
        
        user = self.model(
            phone = phone,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, first_name, last_name, password):
        user = self.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user 
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, verbose_name="What is your contact no.?", unique=True, primary_key=True)
    first_name = models.CharField(max_length=20, verbose_name="What is your first name?")
    last_name = models.CharField(max_length=20, verbose_name="What is your last name?")
    
    # date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
    


    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        first = self.first_name
        last = self.last_name
        fullname = str(first) + ' ' + str(last)
        return fullname

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
