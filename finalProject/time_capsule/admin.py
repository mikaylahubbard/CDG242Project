from django.contrib import admin

# Register your models here.

from .models import LetterCapsule, QuestionCapsule

admin.site.register(LetterCapsule)
admin.site.register(QuestionCapsule)
