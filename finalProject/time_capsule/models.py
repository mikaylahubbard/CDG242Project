from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class LetterCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capsule_name = models.CharField(max_length=255)
    content = models.CharField(max_length=5000)
    date = models.DateField()
    time = models.TimeField()
    locked = models.BooleanField(default=True)
    
    def checkIfLocked(self):
        currentDate = datetime.now().date()
        currentTime = datetime.now().time()
        if currentDate > self.date or (currentDate == self.date and currentTime > self.time):
            self.locked = False
        else:
            self.locked = True
        
        
        
    # string representation of the capsule
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.capsule_name}, Message: {self.content}, Date: {self.date}, Time: {self.time}")
    
class QuestionCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capsule_name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    
    year = models.CharField(max_length=1000, default="empty")
    weather = models.CharField(max_length=1000, default="empty")
    living = models.CharField(max_length=1000, default="empty")
    occupation = models.CharField(max_length=1000, default="empty")
    song = models.CharField(max_length=1000, default="empty")
    book = models.CharField(max_length=1000, default="empty")
    show = models.CharField(max_length=1000, default="empty")
    foods = models.CharField(max_length=1000, default="empty")
    dislikes = models.CharField(max_length=1000, default="empty")
    memory = models.CharField(max_length=1000, default="empty")
    goals = models.CharField(max_length=1000, default="empty")
    best = models.CharField(max_length=1000, default="empty")
    future = models.CharField(max_length=1000, default="empty")
    message = models.CharField(max_length=1000, default="empty")
    
    
    locked = models.BooleanField(default=True)
    
    def checkIfLocked(self):
        currentDate = datetime.now().date()
        currentTime = datetime.now().time()
        if currentDate > self.date or (currentDate == self.date and currentTime > self.time):
            self.locked = False
        else:
            self.locked = True
        
    
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.capsule_name}, Date: {self.date}, Time: {self.time}, Answers: \n - {self.year}\n - {self.weather}\n - {self.living}\n - {self.occupation}\n - {self.song}\n - {self.book}\n - {self.show}\n - {self.foods}\n - {self.dislikes}\n - {self.memory}\n - {self.goals}\n - {self.best}\n {self.future}\n - {self.message}\n")