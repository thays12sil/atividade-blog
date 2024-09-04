from django.contrib import admin

# Register your models here.

from .models import Curso, Gosto

admin.site.register(Curso)
admin.site.register(Gosto)