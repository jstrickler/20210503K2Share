from datetime import datetime
from django import template

register = template.Library()

@register.filter
def truncate(value):
    return 42

# {{ somevar|truncate:"3" }}


@register.simple_tag
def get_current_time():
    return datetime.now().ctime()

# @register.inclusion_tag(takes_context=True, some_object):
# def my_sub_template():
#     returns rendered template
