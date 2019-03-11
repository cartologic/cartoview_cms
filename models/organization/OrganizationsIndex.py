from wagtail.wagtailcore.models import Page


class OrganizationsIndex(Page):
    template = 'cartoview_cms/organization/organizations_index.html'
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.Organization']

    def get_context(self, request):
        # Update context to include only published countries, ordered by reverse-chron
        context = super(OrganizationsIndex, self).get_context(request)
        organizations = self.get_children().live().order_by('-first_published_at')
        context['organizations'] = organizations
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(OrganizationsIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()

    class Meta:
        verbose_name = "Organizations Module"
