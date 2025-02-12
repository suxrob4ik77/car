from django.shortcuts import render

from .models import *

def indexx(request):
    cars=Car.objects.all()
    context={
        'cars':cars,
        'title':'Suxrob_motors'
    }
    return render(request,'Cars/indexx.html',context=context)