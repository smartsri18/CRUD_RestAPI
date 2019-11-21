from django.db import models

# Create your models here.
class EmpDetail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.CharField(max_length=255)
    mobile_no = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
