from django import template
from urllib.parse import urlparse

register = template.Library()


@register.filter
def split(value, arg):
    return value.split(arg)


@register.filter
def parse_url(value):
    return urlparse(value)


@register.filter
def second_last(value):
    try:
        return value[-2]
    except IndexError:
        return ""
