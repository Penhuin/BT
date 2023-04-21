from django.contrib import admin

from .models import UserProfile, UserSocials

admin.site.register(UserProfile)
admin.site.register(UserSocials)
