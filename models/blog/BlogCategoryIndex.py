from wagtail.wagtailcore.models import Page
from .BlogPost import BlogPost


class BlogCategoryIndex(Page):
    template = 'cartoview_cms/blog/blog_category_index.html'
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request):
        # Filter by tag
        category = request.GET.get('category')
        blogposts = BlogPost.objects.filter(categories__name=category)

        # Update template context
        context = super(BlogCategoryIndex, self).get_context(request)
        context['blogposts'] = blogposts
        return context

    def full_clean(self, *args, **kwargs):
        # first call the built-in cleanups (including default slug generation)
        super(BlogCategoryIndex, self).full_clean(*args, **kwargs)
        # now force the slug to be always 'blog-directories'
        self.slug = "blog-categories"

    # Make sure that only one instance is created ever!
    @classmethod
    def can_create_at(cls, parent):
        return super(BlogCategoryIndex, cls).can_create_at(parent) \
               and not cls.objects.exists()
