from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
 


# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=122)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=12)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)