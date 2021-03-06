from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by("-created_at")
    template_name = "articles/article_list.html"
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


class ArticleFormView(LoginRequiredMixin, CreateView):
    template_name = "articles/article_create.html"
    model = Article
    fields = ["title", "image", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "articles/article_create.html"
    fields = ["title", "image", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete_confirm.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False
