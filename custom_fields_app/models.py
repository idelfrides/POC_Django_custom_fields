from django.db import models
from django.utils.translation import gettext_lazy as _
from custom_fields.models import NameField, RoleField
from custom_fields.models import GenderField, CompanyField


class Developer(models.Model):
    full_name = NameField()
    role = RoleField()
    company = CompanyField()
    gender = GenderField()
    age = models.PositiveIntegerField()
    update = models.DateTimeField(
        auto_now=True, 
        auto_now_add=False
    )    

    def __str__(self):
        return self.full_name
    
