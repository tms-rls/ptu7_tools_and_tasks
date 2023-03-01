
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('bills/', views.BillListView.as_view(), name='bills_list_view'),
    path('bills/<int:pk>', views.BillDetailView.as_view(), name='bill_detail_view'),
    path('bills/new', views.BillCreateView.as_view(), name='bill_create_view'),
    path('bills/<int:pk>/update', views.BillUpdateView.as_view(), name='bill_update_view'),
    path('clients/', views.ClientListView.as_view(), name='clients_list_view'),
    path('clients/<int:pk>', views.ClientDetailView.as_view(), name='client_detail_view'),
    path('clients/new', views.ClientCreateView.as_view(), name='client_create_view'),
    path('clients/<int:pk>/update', views.ClientUpdateView.as_view(), name='client_update_view'),
    path('constructionobjects/', views.ConstructionObjectListView.as_view(), name='construction_objects_list_view'),
    path('constructionobjects/<int:pk>', views.ConstructionObjectDetailView.as_view(),
         name='construction_object_detail_view'),
    path('constructionobjects/new', views.ConstructionObjectCreateView.as_view(),
         name='construction_object_create_view'),
    path('constructionobjects/<int:pk>/update', views.ConstructionObjectUpdateView.as_view(),
         name='construction_object_update_view'),
    path('employeetasks/', views.EmployeeTasksListView.as_view(), name="employee_tasks_list"),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail_view'),
    path('tasks/new', views.TaskCreateView.as_view(), name='task_create_view'),
    path('tasks/<int:pk>/update', views.EmployeeTaskUpdateView.as_view(), name='task_update_view'),
    path('tasks/<int:pk>/managerupdate', views.ManagerTaskUpdateView.as_view(), name='task_manager_update_view'),
    path('tools/', views.ToolListView.as_view(), name='tools_list_view'),
    path('employeetools/', views.EmployeeToolsListView.as_view(), name="employee_tools_list"),
    path('tools/<int:pk>', views.ToolDetailView.as_view(), name='tool_detail_view'),
    path('tools/new', views.ToolCreateView.as_view(), name='tool_create_view'),
    path('tools/<int:pk>/update', views.ToolUpdateView.as_view(), name='tool_update_view'),
    path('searchtools/', views.search_tools, name='search_tools'),
    path('searchtasks/', views.search_tasks, name='search_tasks'),
]
