from django import template
register = template.Library()


@register.filter
def addsuffix(strList, suffix):
    return [s + suffix for s in strList]


@register.filter
def addprefix(strList, prefix):
    return [prefix + s for s in strList]
