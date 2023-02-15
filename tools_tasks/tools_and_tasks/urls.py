
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('tools/', views.ToolListView.as_view(), name='tools_list_view'),
    path('tools/<int:pk>', views.ToolDetailView.as_view(), name='tool_detail_view'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail_view'),
    path('constructionobjects/', views.ConstructionObjectListView.as_view(), name='construction_objects_list_view'),
    path('constructionobjects/<int:pk>', views.ConstructionObjectDetailView.as_view(),
         name='construction_object_detail_view'),
    path('searchtools/', views.search_tools, name='search_tools'),
    path('searchtasks/', views.search_tasks, name='search_tasks'),
    path('employeetools/', views.EmployeeToolsListView.as_view(), name="employee_tools_list"),
    path('employeetasks/', views.EmployeeTasksListView.as_view(), name="employee_tasks_list"),
]
