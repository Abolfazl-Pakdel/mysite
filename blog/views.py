from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
  posts = Post.objects.filter(status=1)
  context = {'posts': posts}
  return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
  posts = Post.objects.filter(status=1)
  post = get_object_or_404(posts, pk=pid)
  #
  previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
  #
  next_post = Post.objects.filter(id__gt=post.id).order_by('-id').first()
  context = {'post': post,'previous_post': previous_post,'next_post': next_post}
  return render(request, 'blog/blog-single.html', context)

def test(request, pid):
  # posts = Post.objects.all()
  # post = Post.objects.get(id=pid)
  post = get_object_or_404(Post, pk=pid)
  context = {'post': post}
  return render(request, 'test.html', context)