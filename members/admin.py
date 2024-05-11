from django.contrib import admin
from .models import Position, Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'id_num', 'mobile', 'position')
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
