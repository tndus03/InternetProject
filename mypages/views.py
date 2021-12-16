from django.shortcuts import render

# Create your views here.
def landing(requset):
    return render(
        requset,
        'mypages/landing.html'
    )

def my_page(requset):
    return render(
        requset,
        'mypages/my_page.html'
    )