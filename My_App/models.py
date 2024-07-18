from django.db import models
# Create your models here.
class Student(models.Model):
    roll_num= models.IntegerField()
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    phoneno = models.CharField (max_length=15)

    def __str__(self):
        return self.name
