from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.sname
    
