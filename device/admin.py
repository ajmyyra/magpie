from django.contrib import admin
from .models import Device, DeviceModel, Manufacturer, Vendor

admin.site.register(Device)
admin.site.register(DeviceModel)
admin.site.register(Manufacturer)
admin.site.register(Vendor)
