from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = CKEditor5Field('Description', config_name='extends')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(help_text="Curent Available stock:",default=0)
    reorder_level = models.PositiveIntegerField(default=0) # last rem piece then notif
    mfd_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InventoryTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    notes = CKEditor5Field('Notes', config_name='extends')

    def __str__(self):
        return f"{self.product.name} - {self.get_transaction_type_display()}"
    

class CustomerPurchase(models.Model):

    customer = models.ForeignKey(Patient, blank=True,null=True)
    products = models.ManyToManyField(Product)
    ## auto update
    amount = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    

