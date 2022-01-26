from django.urls import path
from .views import UserSignIn

url_patterns = [
    path('signin', UserSignIn.as_view()),
]
