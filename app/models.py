from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    
    def __str__(self):
        return self.task
    
class History(models.Model):
    new_task = models.CharField(max_length=500)
    desc = models.TextField()
    def __str__(self):
        return self.new_task