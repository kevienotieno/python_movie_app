from django.urls import path
from .views import harvest_list, add_harvest
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_harvest/', views.add_harvest, name='add_harvest'),  # Add harvest page
    path('harvest_list/', views.harvest_list, name='harvest_list'),  
]
