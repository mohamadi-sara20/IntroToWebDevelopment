from django import template

register = template.Library()

@register.filter(name='cut')
def cut(val, arg):
    return val.replace(arg, '')

# register.filter('cut', cut)
