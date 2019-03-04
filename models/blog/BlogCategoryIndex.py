from wagtail.wagtailcore.models import Page
from .BlogPost import BlogPost


class BlogCategoryIndex(Page):
    template = 'cartoview_cms/blog/blog_category_index.html'
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        category = request.GET.get('category')
        blogposts = BlogPost.objects.filter(categories__name=category)

        # Update template context
        context = super(BlogCategoryIndex, self).get_context(request)
        context['blogposts'] = blogposts
        return context
