from rest_framework import routers
from device.viewsets import DeviceViewSet, DeviceModelViewSet, ManufacturerViewSet, VendorViewSet

router = routers.DefaultRouter()

router.register(r'device', DeviceViewSet)
router.register(r'devicemodel', DeviceModelViewSet)
router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'vendor', VendorViewSet)
