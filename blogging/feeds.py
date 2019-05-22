from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Posts"
    link = "/"
    description = "Updates on changes to things I like."

    def items(self):
        published = Post.objects.exclude(published_date=None)
        posts = published.order_by('-published_date')
        return posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
