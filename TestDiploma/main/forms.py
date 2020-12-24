from django.forms import ModelForm

from .models import Property, City


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'