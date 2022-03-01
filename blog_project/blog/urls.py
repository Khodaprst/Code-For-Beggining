from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='post-detail-page'),
    
    
    path('Instagram Account', views.instagram, name='Instagram'),
    path('E-mail Account', views.E_mail, name='E-mail'),
    path('Telegram ID', views.Telegram, name='Telegram')
]
