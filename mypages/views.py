from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'mypages/landing.html'
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