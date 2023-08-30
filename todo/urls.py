from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', views.TodoList.as_view(), name='todo_list'),
    path('todos/create/', views.TodoCreate.as_view(), name='todo_create'),
    path('todos/<int:id>/update/', views.TodoUpdate.as_view(), name='todo_update'),
    path('todos/<int:id>/delete/', views.TodoDelete.as_view(), name='todo_delete'),
    path('delete-inactive-todos/', views.TodoDeleteInactive.as_view(), name='delete_inactive_todos')
]
