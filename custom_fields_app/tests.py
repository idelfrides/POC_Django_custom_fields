from django.test import TestCase
from .models import Developer
from .managers import Manager


class DeveloperTestCase(TestCase):
      
    def setUp(self):
        Developer.objects.create(
            full_name='idel',
            role='dev back-end',
            company='Google',
            gender='Mele',
            age='20'
        )
    

    def test_dev_exists(self):
        """Test if dev informed exists on the database"""

        idel = Developer.objects.get(full_name='idel')
        self.assertEqual(idel.full_name, 'IDEL', msg='Test if this dev exists')
        
        man_obj = Manager()
        man_obj.show_date_hour()
