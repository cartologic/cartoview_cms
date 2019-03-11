from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class CaseStudyIndex(Page):
    template = 'cartoview_cms/case_study/case_study_index.html'
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.CaseStudy']

    def get_context(self, request):
        # Update context to include only published case studies, ordered by reverse-chron
        context = super(CaseStudyIndex, self).get_context(request)
        casestudies = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(casestudies, 6)  # Show 6 resources per page
        page = request.GET.get('page')
        try:
            casestudies = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            casestudies = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            casestudies = paginator.page(paginator.num_pages)
        context['casestudies'] = casestudies
        return context

    content_panels = Page.content_panels + [

    ]

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(CaseStudyIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()

    class Meta:
        verbose_name = "Case Studies Module"
