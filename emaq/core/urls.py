from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name="home"),
  path('ubication/',views.ubication,name="ubication"),
  path('contact/',views.contact,name="contact"),
]