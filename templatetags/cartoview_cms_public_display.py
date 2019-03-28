from django import template
from ..models.menu.MenuItem import MenuItem
from ..models.generic_module.GenericModule import GenericModule

register = template.Library()

@register.inclusion_tag('cartoview_cms/templatetags/cartoview_cms_public_display.html')
def cartoview_cms_display_modules():
    modules = None
    modules = GenericModule.objects.filter(public_display=True).all()
    return {'modules': modules}