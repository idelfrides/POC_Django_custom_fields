from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator


class NameField(forms.CharField):
    widget = forms.TextInput(
        attrs={"placeholder": "Enter your name"}
    )
    
    default_validators = [
        MaxLengthValidator(21),
    ]
                
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'pattern': r'[a-zA-Z]+',
            'autocomplete': 'on',
            'autocorrect': 'on',
            'spellcheck': 'off',
            'autocapitalize': 'on',
            'placeholder': "Enter your full name",
        })
        return attrs
    

class CompanyField(forms.CharField):
    widget = forms.TextInput(
        attrs={"placeholder": "Enter your company name"}
    )
    
    default_validators = [
        MaxLengthValidator(51),
    ]
                
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'pattern': r'[a-zA-Z]+',
            'autocomplete': 'on',
            'autocorrect': 'on',
            'spellcheck': 'off',
            'autocapitalize': 'on',
            'placeholder': "Enter your company full name",
        })
        return attrs
