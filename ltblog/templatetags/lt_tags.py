__author__ = 'jxl'

from django import template
from ltblog.models import Category, Entry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag('tags/recently.html')
def  recently():
    entries = Entry.objects.order_by('-pub_date')[0:5]
    return {'entry_list':entries}

@register.inclusion_tag('tags/category.html')
def category():
    category = Category.objects.all()
    return {'category_list' : category}

@register.inclusion_tag('tags/archives.html')
def archives():
    date = Entry.objects.all().dates('pub_date','month',order='DESC')
    return {'dates':date}
