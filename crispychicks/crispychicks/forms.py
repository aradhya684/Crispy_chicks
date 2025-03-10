from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =  User 
        #fields = "__all__" to show all fields
        fields = ['username', 'first_name','last_name','email']
