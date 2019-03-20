from django import template
from ..models.menu.MenuItem import MenuItem
from ..models.general.GeoPage import GeoPage

register = template.Library()

@register.inclusion_tag('cartoview_cms/templatetags/coastal_issues.html')
def display_issues():
    menu_item = MenuItem.objects.filter(slug="coastal-issues").first()
    coastal_issues = GeoPage.objects.live().descendant_of(menu_item).type(GeoPage)
    return {'coastal_issues': coastal_issues}