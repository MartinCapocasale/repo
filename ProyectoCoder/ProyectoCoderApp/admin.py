from django.contrib import admin

from ProyectoCoderApp.models import *
from .models import *

# Register your models here.

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision')#campos que muestra en el panel de admin
    search_fields = ('nombre', 'comision')#opciones de busqueda en el panel de admin


class EstudianteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido')


class ProfesorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'profesion')
    readonly_fields = ('profesion',) #hago que la profesion solo sea read only


class EntregableAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'fechaEntrega', 'entregado')


admin.site.register(Curso,CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)

# admin, admin -> python manage.py createsuperuser