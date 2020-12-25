from django.urls import path, include

from .views import (
    CustomPropertyView,
    HomeView,
    PropertyListView,
    PropertyDetailView,
    PropertyCreateView,
    PropertyView,
    BootstrapFilterView
                    )

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('tallin/', PropertyView.as_view(), name='tallin'),
    path('property_list/',PropertyListView.as_view(), name='property-list'),
    path('create/',PropertyCreateView.as_view(), name='property-create'),
    path('<int:id>',PropertyDetailView.as_view(), name='property-detail'),
    path('property_create/',CustomPropertyView.as_view(), name='property-create'),
    path('',BootstrapFilterView, name='bootstrap'),

]