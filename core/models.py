from django.db import models

# Create your models here.

PRIORITY = (
    ('1', 'Low'),
    ('2', 'Medium'),
    ('3', 'High'),
)

STATUS = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
)

class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    priority = models.CharField(choices=PRIORITY, default="1", null=True, blank=True)
    
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
       verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    
