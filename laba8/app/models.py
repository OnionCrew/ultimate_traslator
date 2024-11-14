from django.db import models

class Error(models.Model):
    description = models.TextField()
    received_date = models.DateField()
    severity = models.CharField(max_length=20)
    category = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)

class Programmer(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

class ErrorFix(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.IntegerField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
