from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.utils.safestring import mark_safe
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page


class GenericModule(Page):
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.GenericPage']
    show_in_menus_default = True

    selected_template = models.CharField(default='cartoview_cms/generic_module/generic_module_default.html',
                                         max_length=255, choices=(
            ('cartoview_cms/generic_module/generic_module_default.html', 'Default Template'),
            ('cartoview_cms/generic_module/generic_module_focused.html', 'Focused Template'),
        ))
    first_title = models.CharField(max_length=120, blank=True, null=True, help_text=mark_safe(
        "You should select the <b>focused template</b> for this to work!"))
    second_title = models.CharField(max_length=120, blank=True, null=True, help_text=mark_safe(
        "You should select the <b>focused template</b> for this to work!"))
    public_display = models.BooleanField(default=False, verbose_name="Public Display",
                                      help_text=mark_safe("If checked, this module's children will be visible in <b>frontend</b>"))
    public_display_title = models.CharField(max_length=120, blank=True, null=True, help_text=mark_safe(
        "You should check the previous field for this to work!"))

    @property
    def template(self):
        return self.selected_template

    def get_context(self, request):
        context = super(GenericModule, self).get_context(request)
        # Update context to include only published child resources, ordered by reverse-chron
        resources = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(resources, 6)  # Show 6 resources per page
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            resources = paginator.page(1)  # If page is not an integer, deliver first page.
        except EmptyPage:
            resources = paginator.page(
                paginator.num_pages)  # If page is out of range (e.g. 9999), deliver last page of results.
        context['resources'] = resources
        return context

    content_panels = Page.content_panels + [
        FieldPanel('selected_template', widget=forms.Select),
        MultiFieldPanel([
            FieldPanel("first_title", classname="full"),
            FieldPanel("second_title", classname="full"),
        ], heading="Focused Information (Focus Template only)"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('public_display'),
        FieldPanel('public_display_title'),
    ]

    class Meta:
        verbose_name = "Generic Module"
