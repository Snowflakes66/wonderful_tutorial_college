from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Subject, Purchase

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'is_standalone', 'standalone_price']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['user', 'purchase_type', 'amount_paid', 'date_purchased', 'is_active']