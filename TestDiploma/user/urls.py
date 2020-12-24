from django.urls import path, include

from django.contrib.auth.models import User
from .views import MySignupView

urlpatterns = [

# path('login', MyLoginView.as_view()),
# path('logout', LogoutView.as_view()),
    path('signup/', MySignupView.as_view()),

]