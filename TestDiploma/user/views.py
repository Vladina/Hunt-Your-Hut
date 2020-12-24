from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'