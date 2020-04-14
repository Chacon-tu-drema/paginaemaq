from django.contrib import admin
from .models import Grua, Serie

# Register your models here.
class GruaAdmin(admin.ModelAdmin):
  readonly_fields=('created', 'updated')

class SerieAdmin(admin.ModelAdmin):
  readonly_fields=('created', 'updated')

admin.site.register(Grua, GruaAdmin)
admin.site.register(Serie, SerieAdmin)
