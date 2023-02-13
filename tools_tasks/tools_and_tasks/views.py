
from django.shortcuts import render
from django.views import generic
from .models import Tool, Task


def start(request):
    return render(request, 'start.html')


class ToolListView(generic.ListView):
    model = Tool
    template_name = 'tools_list.html'
    context_object_name = "tools_list"


class ToolDetailView(generic.DetailView):
    model = Tool
    template_name = 'tool_detail.html'
    context_object_name = "tool_detail"


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = "tasks_list"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = "task_detail"
