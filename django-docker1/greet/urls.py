from django.urls import path
from . views import greet_view
urlpatterns = [
    path('hello/',greet_view, name="greetings" )
]
