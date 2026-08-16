from django.contrib import admin
from profiles.models import Student 
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    search_fields = ('name','city')
    list_filter = ('age','city')
    ordering = ('name',)