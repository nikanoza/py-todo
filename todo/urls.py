from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', views.TodoList.as_view(), name='todo_list'),
]
