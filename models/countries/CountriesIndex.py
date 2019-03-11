from wagtail.wagtailcore.models import Page


class CountriesIndex(Page):
    template = 'cartoview_cms/countries/countries_index.html'
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.Country']

    def get_context(self, request):
        # Update context to include only published countries, ordered by reverse-chron
        context = super(CountriesIndex, self).get_context(request)
        countries = self.get_children().live().order_by('-first_published_at')
        context['countries'] = countries
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(CountriesIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()

    class Meta:
        verbose_name = "Countries Module"
