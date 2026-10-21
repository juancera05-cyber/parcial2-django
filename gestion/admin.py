from django.contrib import admin

from .models import Proyecto, Tarea


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_inicio")
    search_fields = ("nombre",)


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "proyecto", "completada")
    list_filter = ("completada", "proyecto")
    search_fields = ("titulo",)
