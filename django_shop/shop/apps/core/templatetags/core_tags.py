from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('core/tags/navbar.html')
def navbar(**kwargs):
    return kwargs


@register.inclusion_tag('core/tags/main_filter.html')
def main_filter(**kwargs):
    return kwargs


@register.inclusion_tag('core/tags/main_filter.html')
def main_filter(**kwargs):
    return kwargs


@register.simple_tag
def get_settings(conf):
    return getattr(settings, conf)

