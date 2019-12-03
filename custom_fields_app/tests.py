from django.test import TestCase
from custom_fields_app.models import Developer
from .managers import Manager


class DeveloperTestCase(TestCase):
      
    def setUp(self):
        Developer.objects.create(
            full_name='obama',
            role='dev back-end',
            company='Google',
            gender='Male',
            age='200'
        )
    

    def test_dev_exists(self):
        """Test if dev informed exists on the database"""

        idel = Developer.objects.get(full_name='obama')
        
        self.assertEqual(
            idel.full_name, 
            'obama', 
            msg='Test if this dev exists'
        )
        
        manager_obj = Manager()        
        manager_obj.show_date_hour()


