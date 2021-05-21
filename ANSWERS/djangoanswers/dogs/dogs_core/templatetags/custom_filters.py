from datetime import datetime
from django import template

register = template.Library()


# register filter with template system
@register.filter
def fancy(value):
    # returns text which will be inserted in template
    return f"{value.name} ({value.breed})"

# usage:
# {{ dog|fancy }}


# custom tag
@register.simple_tag
def get_current_time():
    return datetime.now().ctime()

# @register.inclusion_tag(takes_context=True, some_object):
# def my_sub_template():
#     returns rendered template
