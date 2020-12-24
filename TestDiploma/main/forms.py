from django.forms import ModelForm
from django import forms
from .models import Property, City


class PropertyForm(ModelForm):
    # address = forms.CharField(label='Address')
    # size = forms.FloatField()
    # price = forms.FloatField()
    # comments = forms.CharField(max_length=255)
    # contact_number = forms.CharField(max_length=16)

    class Meta:
        model = Property
        fields = '__all__'

