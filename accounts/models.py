from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from accounts.managers import UserManager

from django.utils import timezone



class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User.
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    bio = models.TextField(max_length=500, blank=True, null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.email




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=17, blank=True,default='')
    birth_date = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    phone_number = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return self.user.email


    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
        
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()
    #     pass
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
