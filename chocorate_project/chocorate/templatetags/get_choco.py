from django import template
from chocorate.models import Chocolate

register = template.Library()

@register.inclusion_tag('chocorate/categories.html')
def get_chocolate_list():
    print('function called')
    return ['asdsd', 'asde']