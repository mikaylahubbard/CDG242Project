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
from .forms import *



def home(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'home.html', context)

def about(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'about.html', context)

def letters(request):
        if request.method == "POST":
                # Create the capsule
            form = LetterForm(request.POST)
            if form.is_valid():
                capsule_name = form.cleaned_data['capsule_name']
                content = form.cleaned_data['content']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                capsule = LetterCapsule(user=request.user, capsule_name=capsule_name, content=content, date=date, time=time)
                capsule.save()
                
            return redirect("/capsules/")
        else:
            form = LetterForm()
        current_user = request.user
        context = {
            'user': current_user,
            'form': form,
        }
        return render(request, 'letters.html', context)



def form(request):
    if request.method == "POST":
        #create a time capsule
        form = QuestionForm(request.POST)
        if form.is_valid():
            capsule_name = form.cleaned_data['capsule_name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            year = form.cleaned_data['year']
            weather = form.cleaned_data['weather']
            living = form.cleaned_data['living']
            occupation = form.cleaned_data['occupation']
            song = form.cleaned_data['song']
            book = form.cleaned_data['book']
            show = form.cleaned_data['show']
            foods = form.cleaned_data['foods']
            dislikes = form.cleaned_data['dislikes']
            memory = form.cleaned_data['memory']
            goals = form.cleaned_data['goals']
            best = form.cleaned_data['best']
            future = form.cleaned_data['future']
            message = form.cleaned_data['message']
            
            capsule = QuestionCapsule(user=request.user, capsule_name=capsule_name, date=date, time=time, year=year, weather=weather, living=living, occupation=occupation, song=song, 
                                      book=book, show=show, foods=foods, dislikes=dislikes, memory=memory, goals=goals, best=best, future=future, message=message)
            capsule.save()
            
        return redirect("/capsules/")
    else:
        form = QuestionForm()
    current_user = request.user
    context = {
        'user': current_user,
        'form': form,
    }
    return render(request, 'form.html', context)

def capsules(request):
    # display the database contents
    current_user = request.user
    letters = LetterCapsule.objects.filter(user = current_user)
    forms = QuestionCapsule.objects.filter(user=current_user)
    
    for letter in letters:
        letter.checkIfLocked()
    for form in forms:
        form.checkIfLocked()
    
    context = {
        'user': current_user,
        'letters': letters,
        'forms': forms,
    }
    return render(request, 'capsules.html', context)

def create(request):
    if request.method == "POST":
        # Create the capsule
        form = LetterForm(request.POST)
        if form.is_valid():
            capsule_name = form.cleaned_data['capsule_name']
            content = form.cleaned_data['content']
            capsule = LetterCapsule(capsule_name=capsule_name, content=content)
            capsule.save()
            
            return redirect("/capsules/")
    else:
        form = LetterForm()
    current_user = request.user
    context = {
        'user': current_user,
        'form': form,
    }
    
    return render(request, 'createCapsule.html', context)

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
        return redirect('/login/')
    
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


    
