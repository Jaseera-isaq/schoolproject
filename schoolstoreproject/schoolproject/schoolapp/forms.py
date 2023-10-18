from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'department', 'course', 'purpose', 'materials']

