from django.db import models
from django.db.models.fields import AutoField, BooleanField, CharField, EmailField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



class Keyword(models.Model):
    id = AutoField(primary_key=True)
    data = CharField(max_length=500)  

    def __str__(self):
        return self.data

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **kwargs):
        if not username:
            raise ValueError('the given username is not valid')   
        email = self.normalize_email(email)  
        user = self.model(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser, **kwargs)
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_user(self, username, email, password, **kwargs):
        return self._create_user(username, email, password, is_staff=True, is_superuser=False, **kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        user =  self._create_user(username, email, password, True, True, **kwargs) 
        user.save()  
        return user.save(using = self.db) 

class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=200, unique=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]






