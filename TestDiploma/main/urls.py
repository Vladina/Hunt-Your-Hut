from django.urls import path, include

from .views import tallin, home

urlpatterns = [
    path('home/', home, name='home'),
    path('tallin/', tallin, name='tallin')

]