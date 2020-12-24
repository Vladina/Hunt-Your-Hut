from django.shortcuts import render
from .models import City, Property

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def vilnius_page(request):
    context = {'city':City.objects.all(name='Vilnius')}
    return render(request, 'vilnius_page.html', context = context)