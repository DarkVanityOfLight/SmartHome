from django.urls import path
from . import views

urlpatterns = [
    path('Chatt', views.chatt),
]

