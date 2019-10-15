from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _

from . import forms


ROLE_CHOICES = [
    ('BACK-END DEVELOPER', 'Back-end Developer'),
    ('FRONT-END DEVELOPER', 'Front-end Developer'),
    ('FULL STACK DFEVELOPER', 'Full Stack Developer'),
    ('ANDROID DEVELOPER', 'Android Developer'),
    ('IOS DEVELOPER', 'iOS Developer'),
    ('DESIGNER', 'Designer'),
]

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female')
]


class NameField(models.CharField):
    """Custom dev name field """
    
    default_validators = [
        MaxLengthValidator(21),
    ]

    default_error_messages = {
        'invalid': _("'%(value)s' you enter an invalid  name. "
                     "Full name value must be string." ) 
    }
    

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 21)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        try:                
            value_int = int(value)  
        except ValueError:
            # print('\n\n valid')                 # is alpha
            return value                                
        else: 
            print('\n\n invalid ', value_int)   # is numeric
            raise ValidationError(_('Full name value must be a string .'))   
        finally:
            pass

    def formfield(self, **kwargs):            
        return super().formfield(**{
            'form_class': forms.NameField,
            **kwargs,
        })


class RoleField(models.CharField):  
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', ROLE_CHOICES)
        super().__init__(*args, **kwargs)

    def to_python(self, value):   
        return super().to_python(value)          
    
    def formfield(self, **kwargs):
        return super().formfield(**kwargs)


class CompanyField(models.CharField):
    """ Custom dev company name field """
    
    default_validators = [
        MaxLengthValidator(51),
    ]

    default_error_messages = {
        'invalid': _("'%(value)s' you enter an invalid  name. "
                     "Full name value must be string." ) 
    }
    
    description = _("Enter your name")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 51)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        try:                
            value_int = int(value)  
        except ValueError:
            return value                                
        else: 
            print('\n\n invalid ', value_int)   # is numeric
            raise ValidationError(_('Company name value must be a string .'))   
        finally:
            pass

    def formfield(self, **kwargs):            
        return super().formfield(**{
            'form_class': forms.CompanyField,
            **kwargs,
        })


class GenderField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 6)
        kwargs.setdefault('choices', GENDER_CHOICES)
        super().__init__(*args, **kwargs)

    def to_python(self, value):   
        return super().to_python(value)  

    def formfield(self, **kwargs):
        return super().formfield(**kwargs)