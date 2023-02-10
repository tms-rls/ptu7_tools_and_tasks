
from django.contrib import admin

from .models import Bill, Client, Employee, ConstructionObject, Task, Tool


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'inventory_number', 'employee', 'construction_object', 'status')
    list_filter = ('name', 'employee', 'construction_object', 'status')
    fieldsets = (
        ('General information', {'fields': ['inventory_number']}),
        ('Availability', {'fields': ('status', 'employee', 'construction_object')})
    )


admin.site.register(Bill)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(ConstructionObject)
admin.site.register(Task)
admin.site.register(Tool, ToolAdmin)
