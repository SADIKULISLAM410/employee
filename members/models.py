from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    id_num = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    
