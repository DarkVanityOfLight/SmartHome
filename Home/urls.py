from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home_View, name='home'),
    url('Home', views.home_View),
    url('Pinnboard', views.create_pinned_View, name="Pinnboard"),
]
