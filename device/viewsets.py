from rest_framework import viewsets
from .models import Device, DeviceModel, Manufacturer
from .serializers import DeviceSerializer, DeviceModelSerializer, ManufacturerSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

