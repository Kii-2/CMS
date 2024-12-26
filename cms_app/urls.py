from django.urls import path
from .views import DeviceListView, LeadCreateView, home_view

urlpatterns = [
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('leads/', LeadCreateView.as_view(), name='lead-create'),
    path('home/',home_view, name = 'home' )
]
