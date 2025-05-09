from django.urls import path
from . import views
# from django.contrib.auth import views as auth

from django.contrib import admin  # Django admin module
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('capsules/', views.capsules, name='capsules'),
    path('letters/', views.letters, name='letters'),
    path('form/', views.form, name='form'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('viewletter/<int:letter_id>', views.viewLetter, name='view_letter'),
    path('viewform/<int:form_id>', views.viewForm, name='view_form'),
] 
#  Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

