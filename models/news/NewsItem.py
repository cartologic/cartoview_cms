from django import forms
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalManyToManyField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from .NewsItemTag import NewsItemTag


class NewsItem(Page):
    template = 'cartoview_cms/news/news_item.html'
    parent_page_types = ['cartoview_cms.NewsIndex', 'cartoview_cms.NewsItem']
    subpage_types = ['cartoview_cms.NewsItem']
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=NewsItemTag, blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="News information"),
        FieldPanel('intro'),
        ImageChooserPanel('thumbnail'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
