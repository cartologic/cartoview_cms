from wagtail.wagtailcore.models import Page
from .NewsItem import NewsItem


class NewsTagIndex(Page):
    template = 'cartoview_cms/news/news_tag_index.html'
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        newsitems = NewsItem.objects.filter(tags__name=tag)

        # Update template context
        context = super(NewsTagIndex, self).get_context(request)
        context['newsitems'] = newsitems
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(NewsTagIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()
