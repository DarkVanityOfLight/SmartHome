from django.shortcuts import render
from .models import important_thing
from .forms import pinned_message_form
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_View(request):

    context = {'messages': important_thing.objects.all()}
    return render(request, 'Home/index.html', context)


@login_required
def create_pinned_View(request):
    
    if request.method == "POST":
        form = pinned_message_form(request.POST)
        if form.is_valid():
            
            date = form.cleaned_data['Datum']
            _body = form.cleaned_data['body']
            sender = request.user
            
            pinn_obj = important_thing(Datum = date, body=_body, Ersteller=sender)
            pinn_obj.save()
            
            return HttpResponseRedirect('/Home')

    else:
        form = pinned_message_form()

    context = {'form': form}
    return render(request, "Home/create_pinned.html", context)
