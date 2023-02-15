
from django.contrib import admin

from .models import Bill, Client, ConstructionObject, Task, Tool


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
    fields = ('date', 'title', 'deadline', 'status')
    readonly_fields = ('date', )
    extra = 0


class ToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'inventory_number', 'employee', 'construction_object', 'status')
    list_filter = ('title', 'employee', 'construction_object', 'status')
    fieldsets = (
        ('General information', {'fields': ('inventory_number', )}),
        ('Availability', {'fields': ('status', 'employee', 'construction_object')})
    )


class ConstructionObjectAdmin(admin.ModelAdmin):
    inlines = [ToolInline, BillInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_phone')
    inlines = [ConstructionObjectInline, BillInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'employee', 'deadline', 'status')


class BillAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'client', 'amount', 'status')


admin.site.register(Bill, BillAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ConstructionObject, ConstructionObjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Tool, ToolAdmin)
