from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleFormView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail-article"),
    path(
        "article/<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"
    ),
    path("add_article/", ArticleFormView.as_view(), name="add_article"),
    path(
        "article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete"
    ),
]
