
from django.shortcuts import render
from django.views import generic
from .models import Tool


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
