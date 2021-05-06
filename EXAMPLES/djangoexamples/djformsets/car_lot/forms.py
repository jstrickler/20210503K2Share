from django import forms
from .models import Car


# not needed:
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year']


CarFormSet = forms.modelformset_factory(
    Car, fields=['make', 'model', 'year'], extra=2
)
