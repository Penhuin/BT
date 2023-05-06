from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    user_bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))
    
    class Meta:
        model = UserProfile
        fields = ('user_bio',)