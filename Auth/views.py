from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import  authenticate, login, logout

# Create your views here.
def login_View(request):
	
	next = request.GET.get('next', 'Home')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
				
			else: 
				HttpResponse("Inactiv user.")
				
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
			
			 
	
	
	return render(request, "Auth/login.html,"{'redirect': next})
	
	

