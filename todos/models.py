from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 50)
    due_date = models.DateField(max_length = 50)