from django.db import models
from account.models import Profile


class Position(models.Model):
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.position} - {self.department}'


class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    birth_date = models.DateField()
    salary = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname} - {self.position}'


