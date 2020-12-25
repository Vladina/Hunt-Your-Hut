from django.urls import path, include

from .views import (
    PropertyListView,
    PropertyView,
    BootstrapFilterView
                    )

urlpatterns = [
    path('tallin/', PropertyView.as_view(), name='tallin'),
    path('property_list/',PropertyListView.as_view(), name='property-list'),
    path('',BootstrapFilterView, name='bootstrap'),
]