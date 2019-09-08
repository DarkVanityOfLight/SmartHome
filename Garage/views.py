from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import GaragenForm
from django.contrib.auth.decorators import login_required

import gpiozero, time, threading

# Create your views here.
@login_required
def Garage(request):

    def get_user_input():

        if request.method == "POST":
            
            values = GaragenForm(request.POST)
            if values.is_valid():
                SollStatus = values.cleaned_data['SollStatus']

                return SollStatus
        

    def gpio_out(SollStatus):
        Auf = gpiozero.LED(19)
        Zu = gpiozero.LED(26)
        Zu.off()
        Auf.off()

        if SollStatus == 'Auf':
            print('Auf')
            Auf.on()
            time.sleep(1)
            Auf.off()
        elif SollStatus == 'Zu':
            print('Zu')
            Zu.on()
            time.sleep(1)
            Zu.off()
        else:
            print("Something went wrong")


    def gpio_in():
        input = gpiozero.InputDevice(7)
        try:
            if input.is_active():
                return 'Auf'
            else:
                return "Zu"
        except:
            return 'Zu'


    user_in = get_user_input()
    status = gpio_in()
    t1 = threading.Thread(target=gpio_out, args=(user_in,))


    if user_in != status:
        t1.start()


    context = {'forms': GaragenForm(), 'IstStatus': status}
    return render(request, 'Garage/index.html', context)

