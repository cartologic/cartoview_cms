from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class NewsIndex(Page):
    template = 'cartoview_cms/news/news_index.html'
    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['cartoview_cms.NewsItem']
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(NewsIndex, self).get_context(request)
        newsitems = self.get_children().live().order_by('-first_published_at')
        context['newsitems'] = newsitems
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(NewsIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()
