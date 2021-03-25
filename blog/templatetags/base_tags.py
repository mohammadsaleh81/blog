from datetime import datetime, timedelta

from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, Q, Avg
from setuptools.command.register import register

from ..models import Category, Article

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
	return {
		"category": Category.objects.filter(status=True)
	}


@register.inclusion_tag("blog/partials/side_bar.html")
def popular_articles():
	last_month = datetime.today() - timedelta(days=30)
	return {
		"articles":  Article.objects.published().annotate(
			count=Count('hits', filter=Q(articlehit__created__gt=last_month))
	).order_by('-count','-publish')[0:5],
	"title":  "مقالات پربازدید ماه"
	}


@register.inclusion_tag("blog/partials/side_bar.html")
def hot_articles():
	last_month = datetime.today() - timedelta(days=30)
	content_type_id = ContentType.objects.get(app_label='blog', model='article').id
	return {
		"articles":  Article.objects.published().annotate(
			count=Count('comments', filter=Q(comments__posted__gt=last_month) & Q(comments__content_type_id=content_type_id) )
	).order_by('-count','-publish')[:5],
	"title":  "پربحث ترین مقالات ماه"
	}


@register.inclusion_tag("blog/partials/side_bar.html")
def top_articles():
	last_month = datetime.today() - timedelta(days=30)
	content_type_id = ContentType.objects.get(app_label='blog', model='article').id
	return {
		"articles":  Article.objects.published().annotate(
			count=Count('average', filter=Q(rating__content_type_id=content_type_id) )
	).order_by('-count','-publish')[:5],
	"title":  "پربحث ترین مقالات ماه"
	}



@register.inclusion_tag('registration/partials/link.html')
def link(request, link_name, content, classes):
	return {
		'request' : request,
		'link_name': link_name,
		'link': 'account:{}'.format(link_name),
		'content': content,
		'classes' : classes
	}
