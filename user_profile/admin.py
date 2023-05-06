from django.contrib import admin

from .models import UserProfile, UserSocials, UserYT
from .forms import UserProfileForm

class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserSocials)
admin.site.register(UserYT)
