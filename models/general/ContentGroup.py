from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page

from geonode.base.models import TopicCategory
from .ContentCategory import ContentCategory
from .GeoPage import GeoPage


class ContentGroup(Page):
    template = 'cartoview_cms/general/content_group.html'
    subpage_types = ['cartoview_cms.GeoPage']
    show_in_menus_default = True
    content_category = models.ForeignKey('cartoview_cms.ContentCategory', on_delete=models.PROTECT)
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content_category', widget=forms.Select),
    ]

    def get_context(self, request):
        context = super(ContentGroup, self).get_context(request)
        # Filter by category title
        groupcontent = GeoPage.objects.filter(category__identifier=self.title)
        paginator = Paginator(groupcontent, 6)  # Show 6 resources per page
        page = request.GET.get('page')
        try:
            groupcontent = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            groupcontent = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            groupcontent = paginator.page(paginator.num_pages)
        context['groupcontent'] = groupcontent
        return context

    def save(self, *args, **kwargs):
        ContentCategory.assure_category_exists(self.content_category.name)
        category = TopicCategory.objects.filter(identifier=self.content_category.name).first()
        self.category = category
        super(ContentGroup, self).save()
