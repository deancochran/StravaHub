from django.shortcuts import render
from .models import Post

# Create your views here.

def index_view(request):
    """
    This view displays all the blog posts that have been made
    """
    post_objs = Post.objects.all()
    context={
            'posts':post_objs,
        }
    return render(request, 'blog/blog_index.html', context)
    
def post_detail_view(request, post_slug, *args, **kwargs):
    if Post.objects.filter(slug=post_slug).exists():
        post_obj = Post.objects.get(slug=post_slug)
        context={
            'post':post_obj,
        }
        return  render(request, 'blog/post_detail_view.html', context)
    else:
        return  render(request, 'blog/post_detail404_view.html', {})