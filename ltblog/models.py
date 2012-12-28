from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categroies"


    def __unicode__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, verbose_name="Author")
    pub_date = models.DateTimeField(u'date published')
    category = models.ForeignKey(Category, verbose_name=u'category', related_name='entries')

    num_views = models.IntegerField('views', default=0)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    @models.permalink
    def get_absolute_url(self):
        return ('ltblog_entry', (), {
            "entry_id": self.id
        })

    def __unicode__(self):
        return self.title

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    upload_date = models.DateTimeField(u'date uploaded')