import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    user_bio = models.TextField(blank=True,max_length=200)
    class Meta:  
        verbose_name_plural = 'Edit Bio'
    def __str__(self):
        return self.user_bio
    
class UserSocials(models.Model):
    button_name = models.CharField(blank=True, max_length=25)
    image_icon = models.ImageField(blank=True, upload_to='images/socials')
    button_link = models.CharField(blank=True, max_length=1000)
    text_colour = models.CharField(default="fff", blank=True, max_length=6)

    class Meta:  
        verbose_name_plural = 'Edit Socials'
    def __str__(self):
        return self.button_name
