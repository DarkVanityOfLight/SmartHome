from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [

	url('Login', auth_views.LoginView.as_view(template_name='Auth/login.html'), name="Login"),
	url('Logout', auth_views.LogoutView.as_view(template_name='Auth/logout.html'), name="Logout"),
	
]
