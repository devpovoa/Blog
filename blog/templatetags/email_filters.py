from django import template

register = template.Library()

@register.filter
def email_prefix(value):
    """Retorna apenas a parte antes do @ no e-mail"""
    if value and '@' in value:
        return value.split('@')[0]
    return value
