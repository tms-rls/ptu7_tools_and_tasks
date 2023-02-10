
from django.contrib import admin

from .models import Bill, Client, Employee, ConstructionObject, Task, Tool


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'inventory_number', 'employee', 'construction_object', 'status')
    list_filter = ('name', 'employee', 'construction_object', 'status')
    fieldsets = (
        ('General information', {'fields': ('inventory_number', )}),
        ('Availability', {'fields': ('status', 'employee', 'construction_object')})
    )


class ToolInline(admin.TabularInline):
    model = Tool
    extra = 0


class BillInline(admin.TabularInline):
    model = Bill
    extra = 0


class ConstructionObjectInline(admin.TabularInline):
    model = ConstructionObject
    extra = 0


class ConstructionObjectAdmin(admin.ModelAdmin):
    inlines = [ToolInline, BillInline]


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ToolInline, ]


class ClientAdmin(admin.ModelAdmin):
    inlines = [ConstructionObjectInline, ]


admin.site.register(Bill)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ConstructionObject, ConstructionObjectAdmin)
admin.site.register(Task)
admin.site.register(Tool, ToolAdmin)
