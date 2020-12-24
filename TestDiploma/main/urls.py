from django.urls import path, include

from .views import PropertyView, HomeView, PropertyListView, PropertyDetailView, PropertyCreateView, PropertyUpdateView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('tallin/', PropertyView.as_view(), name='tallin'),
    path('property_list/',PropertyListView.as_view(), name='property-list'),
    path('property_create/',PropertyCreateView.as_view(), name='property-create'),
    path('<int:id>',PropertyDetailView.as_view(), name='property-detail'),
    path('<int:id>',PropertyUpdateView.as_view(), name='property-update'),# main/<model>_list.html

]