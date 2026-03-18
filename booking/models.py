from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    data = models.DateField()
    time = models.TimeField()

    created = models.DateTimeField(auto_now_add=True)