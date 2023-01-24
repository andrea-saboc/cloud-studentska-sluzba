from django.contrib import admin

from .models import Student, Professor

# Register your models here.

class PravniAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(Student, PravniAdmin)
admin.site.register(Professor)