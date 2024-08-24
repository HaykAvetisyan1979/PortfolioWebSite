from django.urls import path
from .views import HomeListView, BlogPost1View

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('blog-post/<int:blog_id>', BlogPost1View.as_view(), name='blog') ,
]