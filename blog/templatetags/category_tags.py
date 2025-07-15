from django import template

register = template.Library()

CATEGORY_COLORS = {
    "news": "badge-news",
    "community": "badge-community",
    "culture": "badge-culture",
    "engineering": "badge-engineering",
    "education": "badge-education",
    "partner": "badge-partner",
    "updates": "badge-updates",
    "security": "badge-security",
}


@register.filter
def category_color(slug):
    """Retorna a classe CSS da cor da categoria"""
    return CATEGORY_COLORS.get(slug, "badge-news")
