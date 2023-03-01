
from django.shortcuts import render, reverse
from django.views import generic
from .models import Bill, Client, ConstructionObject, Task, Tool
from .forms import ConstructionObjectCommentForm, TaskCommentForm, ToolCommentForm, TaskCreateForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin


def start(request):
    return render(request, 'start.html')


def search_tools(request):
    query = request.GET.get('query')
    search_results = Tool.objects.filter(Q(title__icontains=query) | Q(inventory_number__icontains=query))
    return render(request, 'search_tools.html', {'tools_list': search_results, 'query': query})


def search_tasks(request):
    query = request.GET.get('query')
    search_results = Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_tasks.html', {'tasks_list': search_results, 'query': query})


class BillListView(LoginRequiredMixin, generic.ListView):
    model = Bill
    template_name = 'bills_list.html'
    context_object_name = 'bills_list'
    paginate_by = 10
    ordering = '-number'


class BillDetailView(LoginRequiredMixin, generic.DetailView):
    model = Bill
    template_name = 'bill_detail.html'
    context_object_name = 'bill_detail'


class BillCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bill
    fields = ['date', 'number', 'client', 'construction_object', 'amount', 'payment_date', 'status']
    success_url = '/bills/'
    template_name = 'new_bill.html'


class BillUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Bill
    fields = ['date', 'number', 'client', 'construction_object', 'amount', 'payment_date', 'status']
    template_name = 'new_bill.html'

    def get_success_url(self):
        return reverse("bill_detail_view", kwargs={"pk": self.object.id})


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'clients_list.html'
    context_object_name = "clients_list"
    paginate_by = 10
    ordering = 'title'


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client_detail'


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    fields = ['title', 'contact_phone', 'contact_email', 'contact_address']
    success_url = '/clients/'
    template_name = 'new_client.html'


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    fields = ['title', 'contact_phone', 'contact_email', 'contact_address']
    template_name = 'new_client.html'

    def get_success_url(self):
        return reverse("client_detail_view", kwargs={"pk": self.object.id})


class ConstructionObjectListView(LoginRequiredMixin, generic.ListView):
    model = ConstructionObject
    template_name = 'construction_objects_list.html'
    context_object_name = "construction_objects_list"
    paginate_by = 10
    ordering = 'address'


class ConstructionObjectDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
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


class ConstructionObjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = ConstructionObject
    fields = ['address', 'manager', 'client']
    success_url = '/constructionobjects/'
    template_name = 'new_construction_object.html'


class ConstructionObjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ConstructionObject
    fields = ['address', 'manager', 'client']
    template_name = 'new_construction_object.html'

    def get_success_url(self):
        return reverse('construction_object_detail_view', kwargs={"pk": self.object.id})


class TaskDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
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


class EmployeeTasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'employee_tasks_list.html'
    context_object_name = 'employee_tasks_list'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(Q(manager=self.request.user) | Q(employee=self.request.user)).order_by('-date')


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = 'new_task.html'
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.manager = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("task_detail_view", kwargs={"pk": self.object.id})


class EmployeeTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    fields = ['status']
    template_name = 'new_task.html'

    def test_func(self):
        task = self.get_object()
        return task.employee == self.request.user

    def get_success_url(self):
        return reverse("task_detail_view", kwargs={"pk": self.object.id})


class ManagerTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    template_name = 'new_task.html'
    form_class = TaskCreateForm

    def test_func(self):
        task = self.get_object()
        return task.manager == self.request.user

    def get_success_url(self):
        return reverse("task_detail_view", kwargs={"pk": self.object.id})


class ToolListView(LoginRequiredMixin, generic.ListView):
    model = Tool
    template_name = 'tools_list.html'
    context_object_name = "tools_list"
    paginate_by = 10
    ordering = 'inventory_number'


class ToolDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
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


class EmployeeToolsListView(LoginRequiredMixin, generic.ListView):
    model = Tool
    template_name = 'employee_tools_list.html'
    context_object_name = 'employee_tools_list'
    paginate_by = 10
    ordering = 'inventory_number'

    def get_queryset(self):
        return Tool.objects.filter(employee=self.request.user).order_by('inventory_number')


class ToolCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tool
    fields = ['title', 'inventory_number', 'status', 'employee', 'construction_object', 'picture']
    success_url = '/tools/'
    template_name = 'new_tool.html'


class ToolUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tool
    fields = ['title', 'inventory_number', 'status', 'employee', 'construction_object', 'picture']
    template_name = 'new_tool.html'

    def get_success_url(self):
        return reverse("tool_detail_view", kwargs={"pk": self.object.id})
