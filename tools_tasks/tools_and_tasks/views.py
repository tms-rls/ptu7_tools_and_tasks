
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from .models import Tool, Task, ConstructionObject
from .forms import ConstructionObjectCommentForm, TaskCommentForm, ToolCommentForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin


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


class ToolDetailView(FormMixin, generic.DetailView):
    model = Tool
    template_name = 'tool_detail.html'
    form_class = ToolCommentForm
    context_object_name = "tool_detail"

    def get_success_url(self):
        return reverse('tool_detail_view', kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.tool = self.object
        form.instance.employee = self.request.user
        form.save()
        return super(ToolDetailView, self).form_valid(form)


class TaskDetailView(FormMixin, generic.DetailView):
    model = Task
    template_name = 'task_detail.html'
    form_class = TaskCommentForm
    context_object_name = "task_detail"

    def get_success_url(self):
        return reverse('task_detail_view', kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.task = self.object
        form.instance.employee = self.request.user
        form.save()
        return super(TaskDetailView, self).form_valid(form)


class ConstructionObjectListView(generic.ListView):
    model = ConstructionObject
    template_name = 'construction_objects_list.html'
    context_object_name = "construction_objects_list"
    paginate_by = 10
    ordering = 'address'


class ConstructionObjectDetailView(FormMixin, generic.DetailView):
    model = ConstructionObject
    template_name = 'construction_object_detail.html'
    form_class = ConstructionObjectCommentForm
    context_object_name = "construction_object_detail"

    def get_success_url(self):
        return reverse('construction_object_detail_view', kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.construction_object = self.object
        form.instance.employee = self.request.user
        form.save()
        return super(ConstructionObjectDetailView, self).form_valid(form)


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


class ToolCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tool
    fields = ['title', 'inventory_number', 'status', 'employee', 'construction_object', 'picture']
    success_url = '/tools/'
    template_name = 'new_tool.html'

    def form_valid(self, form):
        form.instance.employee = self.request.user
        form.save()
        return super().form_valid(form)
