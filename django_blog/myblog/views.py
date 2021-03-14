from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    categories = Category.objects.all()
    queryset = Post.objects.all()
    # 2 means 1 page contain 2 post
    paginator = Paginator(queryset, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'index.html', context)


def blog(request, blog_id):
    new_blog = get_object_or_404(Post, id=blog_id)
    context = {
        'blog': new_blog,
    }
    return render(request, 'blog.html', context)


def category_view(request, cats):
    category_post = Post.objects.filter(categories__title__contains=cats)
    context = {
        'cats': cats,
        'category_post': category_post,
    }
    return render(request, 'categories.html', context)
