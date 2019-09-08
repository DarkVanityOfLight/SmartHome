from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import chatt_Form
from .models import message
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chatt(request):

        user = request.user 

        if request.method == "POST":
            form = chatt_Form(request.POST)
            if form.is_valid():
                
                _Nachricht = form.cleaned_data['Nachricht']
                
                message_obj = message(Nachricht = _Nachricht, Sender = user)
                message_obj.save()
                
                
                return HttpResponseRedirect('Chatt')
                
                
            
        last_ten = message.objects.all().order_by('-id')[:10]
        reversed_last_ten = reversed(last_ten)

        form = chatt_Form()
        context = {'forms': form, 'messages': reversed_last_ten}
        return render(request, 'Chatt/index.html', context)

