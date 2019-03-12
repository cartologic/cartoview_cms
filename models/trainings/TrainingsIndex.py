from wagtail.wagtailcore.models import Page


class TrainingsIndex(Page):
    template = 'cartoview_cms/trainings/trainings_index.html'
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.Training']

    def get_context(self, request):
        # Update context to include only published trainings, ordered by reverse-chron
        context = super(TrainingsIndex, self).get_context(request)
        trainings = self.get_children().live().order_by('-first_published_at')
        context['trainings'] = trainings
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(TrainingsIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()

    class Meta:
        verbose_name = "Trainings Module"
