from rest_framework import routers
from device.viewsets import DeviceViewSet, DeviceModelViewSet, ManufacturerViewSet

router = routers.DefaultRouter()

router.register(r'device', DeviceViewSet)
router.register(r'devicemodel', DeviceModelViewSet)
router.register(r'manufacturer', ManufacturerViewSet)
