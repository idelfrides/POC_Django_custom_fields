from django.test import TestCase
from .models import Developer


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

        idel = Developer.objects.filter(full_name='idel')
        self.assertEqual(idel, 'IDEL', msg='Test if this dev exists')
