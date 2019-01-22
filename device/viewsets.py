from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Device, DeviceModel, Manufacturer, Vendor
from .serializers import DeviceSerializer, DeviceModelSerializer, ManufacturerSerializer, VendorSerializer

@permission_classes((IsAuthenticated, DjangoModelPermissions, ))
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

@permission_classes((IsAuthenticated, DjangoModelPermissions, ))
class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer

@permission_classes((IsAuthenticated, DjangoModelPermissions, ))
class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

@permission_classes((IsAuthenticated, DjangoModelPermissions, ))
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
