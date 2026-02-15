from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('task/add-task/', views.add_task, name="add_task"),
    path('task/<int:id>/', views.task_detail, name="task_detail"),
    path('task/del-task/<int:id>/', views.del_task, name="del_task"),
    path('task/done-task/<int:id>/', views.done_task, name="done_task"),
    path('task/edit-task/<int:id>/', views.edit_task, name="edit_task"),

    path('filter-task/', views.filter_task, name="filter_task"),
    path('search-task/', views.search_task, name="search_task"),

    path('add-category/', views.add_category, name="add_category"),
]