from django.urls import include, path
from .views import index_view, post_detail_view

urlpatterns = [
    path('', index_view), # Blog - index
    path('post/<slug:post_slug>', post_detail_view, name='post-detail'),
    path('post/None', post_detail_view, name='post-detail')
    ]
