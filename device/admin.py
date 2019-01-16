from django.contrib import admin
from .models import Device, DeviceModel, Manufacturer

admin.site.register(Device)
admin.site.register(DeviceModel)
admin.site.register(Manufacturer)
