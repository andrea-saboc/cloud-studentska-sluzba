from django.contrib import admin

from .models import Student, Professor

# Register your models here.

class PMFAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(Student, PMFAdmin)
admin.site.register(Professor)

