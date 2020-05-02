from django import template
register = template.Library()


@register.filter
def name(obj):
    return obj.__class__.__name__

@register.filter
def fields(obj):
    return obj._meta.concrete_fields