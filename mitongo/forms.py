from django import forms
from .models import RestaurantLocation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
#from crispy_forms.helper import FormHelper



class RestaurantLocationsForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class  RestaurantLocationForm(forms.ModelForm):
    class Meta:
        model   =  RestaurantLocation
        fields  = '__all__'
