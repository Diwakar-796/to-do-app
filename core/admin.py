from django.contrib import admin
from .models import Task, Category

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_editable = ['priority', 'is_done']
    list_display = ['title', 'priority', 'category', 'created_at', 'is_done']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
