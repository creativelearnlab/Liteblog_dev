__author__ = 'jxl'

from django.contrib.sitemaps import Sitemap
from ltblog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Entry.objects.all()


    def lastmod(self, obj):
        return obj.pub_date

