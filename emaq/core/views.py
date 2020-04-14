from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request,"core/home.html")

def ubication(request):
  return render(request,"core/ubication.html")

def contact(request):
  return render(request,"core/contact.html")