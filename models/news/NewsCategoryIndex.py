from wagtail.wagtailcore.models import Page
from .NewsItem import NewsItem


class NewsCategoryIndex(Page):
    template = 'cartoview_cms/news/news_category_index.html'
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        category = request.GET.get('category')
        newsitems = NewsItem.objects.filter(categories__name=category)

        # Update template context
        context = super(NewsCategoryIndex, self).get_context(request)
        context['newsitems'] = newsitems
        return context
