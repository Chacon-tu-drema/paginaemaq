from django.db import models

# Create your models here.
class Historia(models.Model):
  title=models.CharField(verbose_name="Titulo", max_length=200)
  subtitle=models.CharField(verbose_name="Subtitulo", max_length=200)
  content=models.TextField(verbose_name="Contenido")
  image=models.ImageField(verbose_name="Imagen", upload_to="historia")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

  class Meta:
    verbose_name = "historias"
    verbose_name_plural = "historias"
    ordering = ['title']

  def __str__(self):
    return self.title