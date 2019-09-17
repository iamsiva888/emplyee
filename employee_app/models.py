from django.core.validators import MinLengthValidator
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Address(models.Model):
    des = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.des


class Number(models.Model):
    num = models.CharField(null=True, blank=True, max_length=10, validators=[MinLengthValidator(10)])
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



