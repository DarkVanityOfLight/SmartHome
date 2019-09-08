from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home_View, name='home'),
    path('Home', views.home_View),
    path('Pinnboard', views.create_pinned_View, name="Pinnboard"),
]
