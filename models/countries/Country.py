from django import forms
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from ..case_study.CaseStudy import CaseStudy
from ..news.NewsItem import NewsItem

class Country(Page):
    template = 'cartoview_cms/countries/country.html'
    parent_page_types = ['cartoview_cms.CountriesIndex']
    subpage_types = []
    main_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('HTML', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('page_chooser', blocks.PageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        StreamFieldPanel("body", classname="Full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    def get_context(self, request):
        context = super(Country, self).get_context(request)
        case_studies = CaseStudy.objects.filter(categories__in=self.categories.all())
        news_items = NewsItem.objects.filter(categories__in=self.categories.all())
        context['case_studies'] = case_studies
        context['news_items'] = news_items
        return context
