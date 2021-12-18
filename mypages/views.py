from django.shortcuts import render
from shopping.models import Post

# Create your views here.
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'mypages/landing.html',
                  {
                      'recent_posts': recent_posts,
                  }
    )

def my_page(request):
    return render(
        request,
        'mypages/my_page.html'
    )

def my_company(request):
    return render(
        request,
        'mypages/my_company.html'
    )