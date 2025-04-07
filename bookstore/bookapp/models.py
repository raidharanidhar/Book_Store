from django.db import models

# Create your models here.

class bookmodel(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)