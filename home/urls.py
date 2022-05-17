from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.save_commit, name='save_commit'),
    path('response/', views.response_ans, name='response'),
]