
from django.contrib import admin

from .models import Bill, Client, Employee, ConstructionObject, Task, Tool


class ToolInline(admin.TabularInline):
    model = Tool
    extra = 0


class BillInline(admin.TabularInline):
    model = Bill
    extra = 0


class ConstructionObjectInline(admin.TabularInline):
    model = ConstructionObject
    extra = 0


class TaskInline(admin.TabularInline):
    model = Task
    fields = ('date', 'name', 'deadline', 'status')
    readonly_fields = ('date', )
    extra = 0


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'inventory_number', 'employee', 'construction_object', 'status')
    list_filter = ('name', 'employee', 'construction_object', 'status')
    fieldsets = (
        ('General information', {'fields': ('inventory_number', )}),
        ('Availability', {'fields': ('status', 'employee', 'construction_object')})
    )


class ConstructionObjectAdmin(admin.ModelAdmin):
    inlines = [ToolInline, BillInline]


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ToolInline, TaskInline, ConstructionObjectInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_phone')
    inlines = [ConstructionObjectInline, BillInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'employee', 'deadline', 'status')


class BillAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'client', 'amount', 'status')


admin.site.register(Bill, BillAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ConstructionObject, ConstructionObjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Tool, ToolAdmin)
