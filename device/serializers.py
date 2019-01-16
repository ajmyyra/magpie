from rest_framework import serializers
from .models import Device, Manufacturer, DeviceModel, Vendor

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class DeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model: DeviceModel
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model: Vendor
        fields = '__all__'