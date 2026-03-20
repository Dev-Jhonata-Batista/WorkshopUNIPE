from django.urls import path
from . import views

urlpatterns = [
    path('indedx/', views.home, name='home')
]