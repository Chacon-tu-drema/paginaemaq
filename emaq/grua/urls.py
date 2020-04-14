from django.urls import path
from . import views

urlpatterns = [
  path('',views.serie,name="serie"),
  path('gruas/<int:serie_id>/',views.grua,name='grua')
]