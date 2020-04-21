from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Serie(models.Model):
  name=models.SlugField(verbose_name="Nombre Serie", max_length=100, unique=True)
  content = RichTextField(verbose_name="Resumen")
  image=models.ImageField(verbose_name="Imagen",upload_to="grua/serie")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

  class Meta:
    verbose_name = "serie"
    verbose_name_plural = "series"
    ordering = ['name']

  def __str__(self):
    return self.name

class Grua(models.Model):
  name = models.CharField(verbose_name="Nombre Grua", max_length=100, unique=True)
  content = RichTextField(verbose_name="Descripcion")
  maxalto = models.DecimalField(verbose_name="Alto Maximo", max_digits=5, decimal_places=1)
  maxlargo = models.DecimalField(verbose_name="Largo Maximo", max_digits=5, decimal_places=1)
  maxcarga = models.DecimalField(verbose_name="Carga Maximo", max_digits=5, decimal_places=1)
  image = models.ImageField(verbose_name="Imagen",upload_to="grua/grua/imagen")
  doc = models.FileField(verbose_name="Ficha Tecnica",upload_to="grua/grua/ficha")
  categories = models.ManyToManyField(Serie, verbose_name="Series", related_name="get_grua")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

  class Meta:
    verbose_name = "grua"
    verbose_name_plural = "gruas"
    ordering = ['name']

  def __str__(self):
    return self.name