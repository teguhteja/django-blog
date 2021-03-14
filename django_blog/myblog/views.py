from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
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
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'index.html', context)


def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog.html', context)
