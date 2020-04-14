from django.contrib import admin
from .models import Historia

# Register your models here.
class HistoriaAdmin(admin.ModelAdmin):
  readonly_fields=('created', 'updated')

admin.site.register(Historia, HistoriaAdmin)