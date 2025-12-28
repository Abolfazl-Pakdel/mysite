from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name="totalposts")
def function(a = 5):
    post = Post.objects.filter(status=1).count()
    return post

@register.simple_tag(name="posts")
def function(a = 5):
    post = Post.objects.filter(status=1)
    return post

@register.filter()
def snippet(value, arg=20):
    return value[:arg] + '...'

# @register.inclusion_tag('popularposts.html')
# def popularposts():
#     posts = Post.objects.filter(status=1).order_by('published_date')
#     return {'posts': posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}