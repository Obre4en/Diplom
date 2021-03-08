from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'articles', views.ArticleViewSet)


urlpatterns = [
        path('', include(router.urls)),
        path("auth/", include("rest_framework.urls")),
]
