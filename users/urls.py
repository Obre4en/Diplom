from django.urls import path
from django.contrib.auth import views
from users import views as user_views


urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="login",),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="logout",),
    path("profile/", user_views.profile, name="profile"),
    path("settings/", user_views.edit_profile, name="settings"),
]
