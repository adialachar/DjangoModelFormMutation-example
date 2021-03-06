from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','linkedin','github','favorite_sport')