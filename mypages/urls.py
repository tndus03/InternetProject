from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),    # 서버IP/
    path('my_page/', views.my_page),    # 서버IP/my_page/
]