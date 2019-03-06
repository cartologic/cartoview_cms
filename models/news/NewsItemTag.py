from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


class NewsItemTag(TaggedItemBase):
    content_object = ParentalKey('NewsItem', related_name='tagged_items')
