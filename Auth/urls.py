from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [

	path('Login', auth_views.LoginView.as_view(template_name='Auth/login.html'), name="Login"),
	path('Logout', auth_views.LogoutView.as_view(template_name='Auth/logout.html'), name="Logout"),
	
]
