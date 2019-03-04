from wagtail.wagtailcore.models import Page
from .BlogPost import BlogPost


class BlogTagIndex(Page):
    template = 'cartoview_cms/blog/blog_tag_index.html'
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogposts = BlogPost.objects.filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndex, self).get_context(request)
        context['blogposts'] = blogposts
        return context

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(BlogIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()
