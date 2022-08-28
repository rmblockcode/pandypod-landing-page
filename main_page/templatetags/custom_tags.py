from django import template

register = template.Library()

@register.filter
def mod(num, val):
    return num % val


@register.filter
def len_mod(list, val):
    return len(list) % val
