
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('tools/', views.ToolListView.as_view(), name='tools_list_view'),
    path('tools/<int:pk>', views.ToolDetailView.as_view(), name='tool_detail_view'),
    path('tasks/', views.TaskListView.as_view(), name='tasks_list_view'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail_view'),
]
