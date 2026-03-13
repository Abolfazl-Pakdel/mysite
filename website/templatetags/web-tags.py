from django import template
from blog.models import Post

register = template.Library()
@register.inclusion_tag('website/web-latestposts.html')
def latest_post_index ():
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    return {'posts': posts}

@register.filter
def snippet(value, arg=20):
    return value[:arg] + '...'