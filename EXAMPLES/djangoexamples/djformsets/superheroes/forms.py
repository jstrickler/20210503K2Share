#!/usr/bin/env python
# (c) 2016 CJ Associates
#
from django.forms import Form, CharField, formset_factory

class HeroForm(Form):

    hero_name = CharField(label='Hero', max_length=40)
    hero_real_name = CharFIeld(label='Real Name', max_length=40)

HeroFormSet = formset_factory(HeroForm, extra=2)

hero_formset = HeroFormSet()



