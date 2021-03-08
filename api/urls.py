from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/users', views.CustomUserViewSet)
router.register(r'api/articles', views.ArticleViewSet)


urlpatterns = [
        path('', include(router.urls)),
        path("auth/", include("rest_framework.urls")),

]
