from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
]
