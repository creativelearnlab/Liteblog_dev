__author__ = 'jxl'


from django.contrib.syndication.views import Feed


from ltblog.models import Entry

class LatestFeed(Feed):
    title = ''
    description = ''
    link = 'http://example.net/'


    def items(self):
        return Entry.objects.order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_description(self,item):
        return item.content

    def item_link(self, item):
        return item.get_absolute_url()
