#!/usr/bin/env python
# (c) 2016 CJ Associates
#
from django import forms
from .models import Superhero, City
from .validators import small_integer_only

class LittleIntegerField(forms.IntegerField):
    default_validators = [small_integer_only]


class DemoForm(forms.Form):
    demo_boolean = forms.BooleanField(label="Boolean Value")
    demo_char = forms.CharField(max_length=10, strip=True)
    demo_choice = forms.ChoiceField(choices=[(1, 'A'), (2, 'B'), (3, 'C')])
    demo_date = forms.DateField(label="Date")
    demo_email = forms.EmailField(label="Electronic mail address:",
                                  widget=forms.TextInput(attrs={
                          'placeholder': 'joe@spam.com'
                                  }))
    demo_float = forms.FloatField(help_text="Please enter a floating point number")
    demo_int1 = LittleIntegerField(widget=forms.TextInput(attrs={
        "class": 'myclass',
        "foo": 'bar',
    }))
    demo_int2 = LittleIntegerField()
    demo_int3 = forms.IntegerField(validators=[small_integer_only])
    demo_regex = forms.RegexField(regex=r'(?i)^a[a-z]{1,5}$')
    # submit = forms

    # add clean function here...
    def clean_demo_boolean(self):
        # process field between submission and is_valid()
        bool_value = self.cleaned_data['demo_boolean']
#        raise forms.ValidationError("That is an invalid Boolean")
        return  not bool_value


COLORS = 'green red blue purple orange'.split()
COLOR_CHOICES = [(c.title(), c) for c in COLORS]


class HeroForm(forms.Form):

    hero_name = forms.CharField(label='Hero', max_length=40)
    hero_color = forms.ChoiceField(
        label="Color",
        choices=COLOR_CHOICES,
    )


class HeroModelForm(forms.ModelForm):
    # dog = forms.CharField(max_length=32)
    class Meta:
        model = Superhero
        fields = ['name', 'real_name', 'city', 'secret_identity']
        labels = {
            'name': 'Hero Name',
            'city': 'City where they hang out',
        }


class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        # exclude = ['a', 'b', 'c']  # fields to exclude
