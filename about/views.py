from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def AboutUs(request):
    return render(request,'about.html')
