from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('explore/', views.explore, name='explore'),
    
]
