from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),    # 서버IP/
    path('my_page/', views.my_page),    # 서버IP/my_page/
    path('my_company/', views.my_company),    #서버IP/my_company/
]