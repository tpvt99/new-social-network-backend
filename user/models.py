from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
import uuid
from django.utils import timezone

from page.models import City, Country

# Country code


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, fullname, password = None):
        if not email:
            raise ValueError('Users must have an email adress')
        
        user = self.model(
                email = self.normalize_email(email),
                fullname = fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, nationality, fullname):
        nationality = Country.objects.get(country_code__exact = nationality)
        user = self.create_user(
                email,
                password = password,
                fullname = fullname)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length = 255, unique = True)
    fullname = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    date_joined = models.DateTimeField(auto_now_add = True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS = ['fullname']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class User(models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    fullname = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(default = timezone.now)

def user_profilepic_upload(instance, filename):
    return 'user_{0}/profilepicture/{1}'.format(instance.user.id, filename)

def user_backgroundpic_upload(instance, filename):
    return 'user_{0}/backgroundpic/{1}'.format(instance.user.id, filename)

class Authentication(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 100, null = True)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profilename = models.CharField(max_length = 100, unique = True)

class Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = user_profilepic_upload, null = True)
    birthday = models.DateTimeField(null = True)
    age = models.IntegerField(null = True)
    sex = models.CharField(max_length = 100, null = True)
    bio = models.CharField(max_length = 100, null = True)
    head = models.CharField(max_length = 100, null = True)
    firstname = models.CharField(max_length = 100, null = True)
    lastname = models.CharField(max_length = 100, null = True)
    background_pic = models.ImageField(upload_to = user_backgroundpic_upload, null = True)

class InfoWork(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    company = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200, null = True)
    privacy = models.CharField(max_length = 50) # public,private,friend
    time_begin = models.DateField(null = True)
    time_end = models.DateField(null = True)
    is_working = models.BooleanField(default = 0) #0 is not #1 is working
    

class InfoEducationUniversity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    university = models.CharField(max_length = 200)
    time_begin = models.DateField(null = True)
    time_end = models.DateField(null = True)
    is_graduated = models.BooleanField(default = 0)
    major = models.CharField(max_length =100, null = True)
    privacy = models.CharField(max_length = 100) 

class InfoEducationSchool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    school = models.CharField(max_length = 200)
    time_begin = models.DateField(null = True)
    time_end = models.DateField(null = True)
    is_graduated = models.BooleanField(default = 0)
    privacy = models.CharField(max_length = 100) 

class LivePlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    place = models.CharField(max_length = 100)
    privacy = models.CharField(max_length = 100)

class BornPlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    place = models.CharField(max_length = 100, blank = True, null = True)
    privacy = models.CharField(max_length = 100, blank = True, null = True)

class Activity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    total_activity = models.IntegerField(default = 0)

class Event(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    total_event = models.IntegerField(default = 0)

class EmailValidation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    hash_keyword = models.CharField(max_length = 50)
    has_validate = models.BooleanField(default = False)
