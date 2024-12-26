from django.contrib.auth.models import User
from django.db import models

# Extend the Site model
class Site(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
   

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    managed_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='devices/')
    currency = models.CharField(max_length=10)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    sourced = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=100, null=True, blank=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In-progress', 'In-progress'),
        ('Converted', 'Converted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class WalkIn(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    walk_in_date_time = models.DateTimeField(auto_now_add=True)
    token_number = models.PositiveIntegerField()

# Extend the Page and PageSection models
class WebPage(models.Model):
    title = models.CharField(max_length=100)
    allowed_devices = models.ManyToManyField(Device)

class PageSection(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sections/')
    html_content = models.TextField()
    order = models.PositiveIntegerField()
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
