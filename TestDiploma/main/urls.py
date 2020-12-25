from django.urls import path, include

from .views import (
    HomeView,
    PropertyListView,
    PropertyView,
    BootstrapFilterView
                    )

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('tallin/', PropertyView.as_view(), name='tallin'),
    path('property_list/',PropertyListView.as_view(), name='property-list'),
    path('',BootstrapFilterView, name='bootstrap'),

]