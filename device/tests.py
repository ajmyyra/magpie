from django.test import TestCase
from device.models import Device, Manufacturer, DeviceModel, Vendor
from device.models import DEVICE_STATUSES, DEVICE_TYPE, DEVICE_OWNERSHIP
from django.db.models.deletion import ProtectedError
from django.contrib.auth.models import User

class ManufacturerTests(TestCase):
    def setUp(self):
        new_manufacturer = Manufacturer(name='Apple')
        new_manufacturer.save()
 
    def tearDown(self):
        Manufacturer.objects.filter().delete()
    
    def test_manufacturer_actions(self):
        manufacturers = Manufacturer.objects.filter(name='Apple')
        if not manufacturers:
            self.fail('Manufacturer not available in saved manufacturers.')

        saved_manufacturer = Manufacturer.objects.filter(name='Apple')[0]
        saved_manufacturer.name = 'Äpple'
        saved_manufacturer.save()
        manufacturers = Manufacturer.objects.filter(name='Äpple')
        if not manufacturers:
            self.fail('Manufacturer with changed name not available in saved manufacturers.')


        Manufacturer.objects.filter(name='Äpple').delete()
        manufacturers = Manufacturer.objects.all()
        if manufacturers:
            self.fail('Manufacturer should be deleted already.')


class DeviceModelTests(TestCase):
    def setUp(self):
        new_manufacturer = Manufacturer(name='Apple')
        new_manufacturer.save()
        new_devicemodel = DeviceModel(name='Macbook Pro, Early 2018', manufacturer=new_manufacturer, device_type=DEVICE_TYPE[0])
        new_devicemodel.save()
    
    def tearDown(self):
        DeviceModel.objects.filter().delete()
        Manufacturer.objects.filter().delete()

    def test_devicemodel_integrity(self):
        try:
            Manufacturer.objects.filter(name='Apple').delete()
            self.fail('Deleting protected manufacturer should cause problems.')
        except ProtectedError:
            pass



class VendorTests(TestCase):
    def setUp(self):
        new_vendor = Vendor(name='Jens PC Store', address='Street 12', postal_code='012345', city='Åbo', country='Sweden')
        new_vendor.save()
    
    def tearDown(self):
        Vendor.objects.filter().delete()
    
    def test_vendor_address_change(self):
        vendor = Vendor.objects.filter(address='Street 12')[0]
        vendor.address = 'Another street 1'
        vendor.save()

        old_address = Vendor.objects.filter(address='Street 12')
        if old_address:
            self.fail('Vendor should already have a new address.')
        
        changed_address = Vendor.objects.filter(address='Another street 1')
        if not changed_address:
            self.fail('Vendor should have a new address.')

class DeviceTests(TestCase):
    def setUp(self):
        new_manufacturer = Manufacturer(name='Apple')
        new_manufacturer.save()
        new_devicemodel = DeviceModel(name='Macbook Pro, Early 2018', manufacturer=new_manufacturer, device_type=DEVICE_TYPE[1])
        new_devicemodel.save()

        new_user = User.objects.create_user('mike')

        new_device = Device(name='New laptop for Mike', owner=new_user, model=new_devicemodel, status=DEVICE_STATUSES[0], ownership=DEVICE_OWNERSHIP[0])
        new_device.save()
    
    def tearDown(self):
        Device.objects.filter().delete()
        DeviceModel.objects.filter().delete()
        Manufacturer.objects.filter().delete()
    
    def test_device_relationships(self):
        current_device = Device.objects.filter(name='New laptop for Mike')[0]
        self.assertEqual(current_device.owner.username, 'mike', msg='Incorrect owner.')

