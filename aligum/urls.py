from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),


    # login

    path('login/', loginUser, name='login'),

    # logout

    path('logout/', logoutUser, name='logout'),

    # READ

    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]