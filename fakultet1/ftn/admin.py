from django.contrib import admin

from .models import Student, Professor

# Register your models here.

class FTNAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(Student, FTNAdmin)
admin.site.register(Professor)