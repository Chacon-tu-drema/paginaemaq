from django.shortcuts import render, get_object_or_404
from .models import Serie, Grua
# Create your views here.

def serie(request):
  series = Serie.objects.all()
  return render(request,"grua/serie.html",{'series':series})

def grua(request, serie_id):
  series = get_object_or_404(Serie, id=serie_id)  
  return render(request,"grua/grua.html", {
    'series':series,
    })
