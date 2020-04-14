from django.shortcuts import render
from .models import Historia
# Create your views here.

def historia(request):
  historias=Historia.objects.all()
  return render(request, "historia/about.html", {'historias':historias})
