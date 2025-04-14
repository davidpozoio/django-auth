from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
