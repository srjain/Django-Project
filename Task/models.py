from django.db import models

# Create your models here.

class file(models.Model):
    file_id = models.CharField(max_length=30)
    
    
