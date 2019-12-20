from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

#UserRegister inherits UserCreationForm and adds more fields for User model
#form.save() in the view is a UserCreationForm method
class UserRegister(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username', 'class':'authinput'}),
            'email' : forms.TextInput(attrs={'placeholder': 'Email', 'class':'authinput'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'First Name', 'class':'authinput'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'authinput'}),
        }
    #Override super class password1 and password2 to add needed variables    
    def __init__(self, *args, **kwargs):
            super(UserRegister, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update({'class':'authinput', 'placeholder':"Password"})
            self.fields['password2'].widget.attrs.update({'class': 'authinput', 'placeholder': "Password Confirm"})