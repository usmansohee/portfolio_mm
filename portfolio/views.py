from django.shortcuts import render

from .models import myProject


# Create your views here.


def home(request):
    obj = myProject.objects.all()
    return render(request, 'home.html', {'obj': obj})
