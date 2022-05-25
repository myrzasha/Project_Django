from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),


    # login

    path('login/', login, name='login'),

    # logout

    path('logout/', logout, name='logout'),

    # READ

    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]