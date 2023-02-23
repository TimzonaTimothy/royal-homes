from django.db import models
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    STATUS = (
        ('Rent','Rent'),
        ('Sale','Sale'),
        ('Sold','Sold'),
    )

    PRO_STATUS = (
        ('Apartment','Apartment'),
        ('House','House'),
        ('Land','Land'),
        ('Others','Others'),
    )
    property_type = models.CharField(max_length=255,choices=PRO_STATUS, blank=True, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, blank=True,null=True)
    price= models.IntegerField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    sqft = models.IntegerField(blank=True, null=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True,null=True)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField(blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name
    

class Contacts(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField(blank=True)
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name