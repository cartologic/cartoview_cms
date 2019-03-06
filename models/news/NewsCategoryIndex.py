from wagtail.wagtailcore.models import Page
from .NewsItem import NewsItem


class NewsCategoryIndex(Page):
    template = 'cartoview_cms/news/news_category_index.html'
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        category = request.GET.get('category')
        newsitems = NewsItem.objects.filter(categories__name=category)

        # Update template context
        context = super(NewsCategoryIndex, self).get_context(request)
        context['newsitems'] = newsitems
        return context

    def full_clean(self, *args, **kwargs):
        # first call the built-in cleanups (including default slug generation)
        super(NewsCategoryIndex, self).full_clean(*args, **kwargs)
        # now force the slug to be always 'blog-directories'
        self.slug = "news-categories"


    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(NewsCategoryIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()
