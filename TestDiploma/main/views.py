from django.shortcuts import render
from .models import City, Property


# Create your views here.

def home(request):
    all_properties = Property.objects.all
    return render(request, 'home.html', {'all':all_properties})


def tallin(request):
    context = Property.objects.filter(location__name='Tallin')
    return render(request, 'tallin.html', context=context)
