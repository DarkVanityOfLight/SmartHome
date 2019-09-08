from django.conf.urls import url
from . import views

urlpatterns = [
    url('Chatt', views.chatt),
]

