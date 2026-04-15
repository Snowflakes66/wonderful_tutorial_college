# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_standalone = models.BooleanField(default=False)
    standalone_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    PURCHASE_TYPE = (
        ('department', 'Department Package'),
        ('standalone', 'Standalone Subject'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_type = models.CharField(max_length=20, choices=PURCHASE_TYPE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.purchase_type}"