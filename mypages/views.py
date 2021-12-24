from django.shortcuts import render
from shopping.models import Post, Category, Comment


# Create your views here.
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'mypages/landing.html',
                  {
                      'recent_posts': recent_posts,
                  }
    )

def my_page(request):
    comments = Comment.objects.order_by('-pk')
    return render(
        request,
        'mypages/my_page.html',
        {
            'comments': comments,
        }
    )

def my_company(request):
    Categories = Category.objects.order_by('-pk')
    return render(
        request,
        'mypages/my_company.html',
        {
        'Categories': Categories,
        }
    )