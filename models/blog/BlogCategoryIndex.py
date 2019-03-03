from wagtail.wagtailcore.models import Page
from .BlogPost import BlogPost


class BlogCategoryIndex(Page):
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        category = request.GET.get('category')
        blogposts = BlogPost.objects.filter(categories__name=category)

        # Update template context
        context = super(BlogCategoryIndex, self).get_context(request)
        context['blogposts'] = blogposts
        return context
