from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView)
from . import views

# url patterns should reference path and views name, can be given custom name to reference

# because there is nothing in the path url for the 'blog/' app home page below, the full url returned is just
# (HOST/), while the url for about is HOST/about/

# url patterns below are handled/displayed by the views.py script

# when using a class view, not only must you import the class, must cast it ".as_view()"
# "pk" below references primary key in the database, by sticking to convetion can just use PK
# instead of custom variable name

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    ]
