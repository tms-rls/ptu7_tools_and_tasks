
from django.shortcuts import render
from django.views import generic
from .models import Tool, Task, ConstructionObject
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


def start(request):
    return render(request, 'start.html')


def search_tools(request):
    query = request.GET.get('query')
    search_results = Tool.objects.filter(Q(title__icontains=query) | Q(inventory_number__icontains=query))
    return render(request, 'search_tools.html', {'tools_list': search_results, 'query': query})


def search_tasks(request):
    query = request.GET.get('query')
    search_results = Task.objects.filter(Q(title__icontains=query) | Q(notes__icontains=query))
    return render(request, 'search_tasks.html', {'tasks_list': search_results, 'query': query})


class ToolListView(generic.ListView):
    model = Tool
    template_name = 'tools_list.html'
    context_object_name = "tools_list"
    paginate_by = 10
    ordering = 'inventory_number'


class ToolDetailView(generic.DetailView):
    model = Tool
    template_name = 'tool_detail.html'
    context_object_name = "tool_detail"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = "task_detail"


class ConstructionObjectListView(generic.ListView):
    model = ConstructionObject
    template_name = 'construction_objects_list.html'
    context_object_name = "construction_objects_list"
    paginate_by = 10
    ordering = 'address'


class ConstructionObjectDetailView(generic.DetailView):
    model = ConstructionObject
    template_name = 'construction_object_detail.html'
    context_object_name = "construction_object_detail"


class EmployeeToolsListView(LoginRequiredMixin, generic.ListView):
    model = Tool
    template_name = 'employee_tools_list.html'
    context_object_name = 'employee_tools_list'
    paginate_by = 10

    def get_queryset(self):
        return Tool.objects.filter(employee=self.request.user).order_by('inventory_number')


class EmployeeTasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'employee_tasks_list.html'
    context_object_name = 'employee_tasks_list'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(employee=self.request.user).order_by('date')
