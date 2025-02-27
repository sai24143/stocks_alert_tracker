from django.db import models

class Stock(models.Model):
    symbol=models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=100)
    price=models.FloatField(null=True, blank=True)
    percent=models.FloatField(null=True, blank=True)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
