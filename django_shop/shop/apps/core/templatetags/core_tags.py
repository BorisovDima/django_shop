from django import template

register = template.Library()

@register.inclusion_tag('core/objects/detail-product.html')
def detail_product_template():
    return {}


@register.inclusion_tag('core/tags/navbar.html')
def navbar(**kwargs):
    return kwargs