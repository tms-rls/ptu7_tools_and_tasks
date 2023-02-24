
from django.contrib import admin

from .models import Bill, Client, ConstructionObject, ConstructionObjectComment, Task, TaskComment, Tool, ToolComment


class ToolInline(admin.TabularInline):
    model = Tool
    fields = ('title', 'inventory_number', 'employee', 'construction_object', 'status')
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
    list_display = ('title', 'inventory_number', 'employee', 'construction_object', 'status', 'display_tool_comments')
    list_filter = ('title', 'employee', 'construction_object', 'status')


class ConstructionObjectAdmin(admin.ModelAdmin):
    list_display = ('address', 'manager', 'display_conobj_comments')
    inlines = [ToolInline, BillInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_phone')
    inlines = [ConstructionObjectInline, BillInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'employee', 'deadline', 'status', 'display_task_comments')


class BillAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'client', 'amount', 'status')


class ConstructionObjectCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'construction_object', 'employee', 'text')


class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'task', 'employee', 'text')


class ToolCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'tool', 'employee', 'text')


admin.site.register(Bill, BillAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ConstructionObject, ConstructionObjectAdmin)
admin.site.register(ConstructionObjectComment, ConstructionObjectCommentAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment, TaskCommentAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(ToolComment, ToolCommentAdmin)
