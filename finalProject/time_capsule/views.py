from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context


# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


def home(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    # return HttpResponse(template.render())
    return render(request, 'home.html', context)

def about(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'about.html', context)

def letters(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'letters.html', context)

def form(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'form.html', context)

def capsules(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'capsules.html', context)

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
    current_user = request.user
    context = {
        'user': current_user,
    }
    # Render the login page template (GET request)
    return render(request, 'login.html', context)

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    current_user = request.user
    context = {
        'user': current_user,
    }
    # Render the registration page template (GET request)
    return render(request, 'register.html', context)

def logout_page(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'logout.html', context)


    
