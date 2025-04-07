from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class LetterForm(forms.Form):
    #capsule content
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'placeholder': "Type your letter here..."}))
    #capsule settings
    capsule_name = forms.CharField(label="Name of Capsule:", max_length=255)
    date = forms.DateField(label="Choose a date", widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]);
    time = forms.TimeField(label="Choose a time", widget=forms.TimeInput(attrs={"type": "time"}))
    
    
     
class QuestionForm(forms.Form):
    
      
    capsule_name = forms.CharField(label="Name of Capsule:", max_length=255)
    date = forms.DateField(label="Choose a date", widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]);
    time = forms.TimeField(label="Choose a time", widget=forms.TimeInput(attrs={"type": "time"}))
    #capsule content
    #general questions
    #year
    year = forms.CharField(label="What is the current year?", widget=forms.TextInput)
    # weather
    weather = forms.CharField(label="What is the weather like?", widget=forms.TextInput)
    # living
    living = forms.CharField(label="Where are you living?", widget=forms.TextInput)
    # occupation
    occupation = forms.CharField(label="What is you occupation?", widget=forms.TextInput)
    #favorites questions
    # song 
    song = forms.CharField(label="What is your current favorite song?", widget=forms.TextInput)
    # book 
    book = forms.CharField(label="What is your favorite book?", widget=forms.TextInput)
    # show
    show = forms.CharField(label="What is your favorite show/movie?", widget=forms.TextInput)
    # foods
    foods = forms.CharField(label="What are some of your favorite foods?", widget=forms.TextInput)
    # dislikes
    dislikes = forms.CharField(label="What are some things you dislike?", widget=forms.TextInput)
    #personal questions
    # memory 
    memory = forms.CharField(label="What is your favorite recent memory?", widget=forms.TextInput)
    # goals 
    goals = forms.CharField(label="What are your current life goals or wishes?", widget=forms.TextInput)
    # best 
    best = forms.CharField(label="What are the best parts of your life right now?", widget=forms.TextInput)
    # future 
    future = forms.CharField(label="What do you think your life will be like when this capsule unlocks?", widget=forms.TextInput)
    # message 
    message = forms.CharField(label="Anything else you would like to tell your future self?", widget=forms.TextInput)
    
    
    #for now, I'm having trouble using these to display the html more concisely
    # generalQs = [year, weather, living, occupation]
    # favoriteQs = [song, book, show, foods, dislikes]
    # personalQs = [memory, goals, best, future, message]
    # allQs = {
    #     'General Questions': generalQs,
    #     'Favorites': favoriteQs,
    #     'Personal Questions': personalQs,
    #          }
  
    
    
    
    
    

