"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label='name',
                           max_length=35)
    description = forms.CharField(label='Description', 
                                  widget=forms.Textarea,
                                  max_length=120,
                                  required=False)
    quantity = forms.IntegerField(label='quantity',
                                  validators=[MaxValueValidator(50), MinValueValidator(0)],
                                  widget=forms.NumberInput(attrs={'type': 'number'}))