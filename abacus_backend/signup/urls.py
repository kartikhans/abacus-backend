from django.urls import path
from .views import UserSignUp, UserSignIn, change_password, show_user_profile, update_user

urlpatterns = [
    path('signup/', UserSignUp.as_view()),
    path('signin/', UserSignIn.as_view()),
    path('userprofile/', show_user_profile.as_view()),
    path('update_user/', update_user.as_view()),
    path('change_password/', change_password.as_view())
]
