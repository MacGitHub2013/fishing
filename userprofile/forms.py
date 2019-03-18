from django.forms import ModelForm
from . models import UserProfile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = UserProfile
        fields =('phone_number','no_of_years_in_fishery','state','district')
    

class ProfileChangeForm(ModelForm):
    class Meta:
        model = UserProfile
        fields =('phone_number','no_of_years_in_fishery','state','district')