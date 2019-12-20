from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth
#django built in forms for auths. UserCreation is edited in account/forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from wallet.models import Wallet
#creates messages for template, https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
from django.contrib import messages
from .forms import UserRegister

#Signup view
#If request = post, validate form, if valid save user and login
def signup(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            #form.save() is a auth.forms method which saves to User model 
            form.save()
            messages.success(request, 'Account created successfully')
            #Authenticate user and login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)
            #creates wallet for user
            # userpk = getattr(new_user, "pk")
            wallet = Wallet(user = new_user)
            wallet.save()
            #Login & redirect
            login(request, new_user)
            return redirect('/')
        else:
            #Throw error message to signup page if not valid
            messages.error(request, form.errors)
            return render(request, 'signup.html', {'form': form})
    form = UserRegister()
    return render(request, 'signup.html', {'form': form})

#Login view
#If Post > authenticate user else render form
def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    #form stores and cleans username and password and authenticate
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      #if the user is authenticated then we log them in and redirect them to the home page
      if user is not None:
        login(request, user)
        return redirect('/')
  form = AuthenticationForm()
  return render(request=request, template_name="login.html", context={"form": form})
    
#Logout View
def logout_request(request):
    logout(request)
    return render(request, 'dwallet/home.html')

#Account view
def account(request):
    return render(request, "dwallet/home.html")
