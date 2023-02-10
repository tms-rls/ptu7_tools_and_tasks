
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('tools/', views.ToolListView.as_view(), name='tools_list_view')
]
