from django import forms
from django.contrib.auth.models import User # importing the user model because you'll be updating the user model
from django.contrib.auth.forms import UserCreationForm # necessary to inherit the base usercreationform form
from .models import Profile

# this class inherits from usercreationform, will be passed into the form
# render area in the register.html template

# specify what the form is overwriting and in meta what models and fields it should use

class UserRegisterForm(UserCreationForm):

    # specify what additional fields we want the usercreationform to have
    email = forms.EmailField()

    # meta class gives nested namespace for configurations, keeping configs in one place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']