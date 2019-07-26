from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment/<int:key>', views.comment_list, name='comment_list'),   
    path('post/comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('post/comment/<int:key>/new/', views.comment_new, name='comment_new'),
    path('post/comment/<int:pk>/<int:key>/edit/', views.comment_edit, name='comment_edit'),
    path('?search_box=',views.search,name = 'search'),
    # url(r'^?$', 'views.search', name='search'),
    ]
