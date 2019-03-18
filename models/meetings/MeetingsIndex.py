from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wagtail.wagtailcore.models import Page


class MeetingsIndex(Page):
    template = 'cartoview_cms/meetings/meetings_index.html'
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.Training']

    def get_context(self, request):
        # Update context to include only published trainings, ordered by reverse-chron
        context = super(MeetingsIndex, self).get_context(request)
        meetings = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(meetings, 6)  # Show 6 resources per page
        page = request.GET.get('page')
        try:
            meetings = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            meetings = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            meetings = paginator.page(paginator.num_pages)
        context['meetings'] = meetings
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(MeetingsIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()

    class Meta:
        verbose_name = "Meetings Module"
