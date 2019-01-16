from django.db import models
from django.contrib.auth.models import User

DEVICE_STATUSES = (
    (u'new', u'New'),
    (u'active', u'In use'),
    (u'shelf', u'Not in use'),
    (u'broken', u'Broken'),
    (u'repair', u'In repair'),
    (u'lost', u'Lost'),
    (u'sold', u'Sold'),
    (u'scrapped', u'Scrapped')
)

DEVICE_OWNERSHIP = (
    (u'org', u'Organisation'),
    (u'user', u'User'),
    (u'ext', u'External organisation')
)

DEVICE_TYPE = (
    (u'desktop', u'Desktop'),
    (u'laptop', u'Laptop'),
    (u'phone', u'Phone'),
    (u'handheld', u'Handheld (tablet etc)'),
    (u'iot', u'IoT device (fridge, lamp controller etc)'),
    (u'other', u'Other')
)

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Name')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Address')
    postal_code = models.IntegerField(blank=True, null=True, verbose_name=u'Postal code')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'City')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'Phone number')

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class DeviceModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name=u'Manufacturer', on_delete=models.PROTECT)
    name = models.CharField(max_length=250, blank=True, null=True)
    device_type = models.CharField(max_length=16, choices=DEVICE_TYPE, verbose_name=u'Device type', default='other', db_index=True)
    comments = models.TextField(verbose_name=u'Comments')


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, verbose_name=u'Owner', on_delete=models.PROTECT, blank=True, null=True)
    model = models.ForeignKey(DeviceModel, verbose_name=u'Model', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, verbose_name=u'Name')
    description = models.TextField(verbose_name=u'Description', max_length=2048, blank=True)
    added = models.DateTimeField(verbose_name=u'Added', auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name=u'Added', auto_now_add=True)
    status = models.CharField(max_length=16, choices=DEVICE_STATUSES, verbose_name=u'Status', default='new', db_index=True)
    ownership = models.CharField(max_length=16, choices=DEVICE_OWNERSHIP, verbose_name=u'Ownership', default='org', db_index=True)
    warranty_until = models.DateField(verbose_name=u'Warranty until', blank=True)

    def __str__(self):
        return self.name
