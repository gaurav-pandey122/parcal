from django.urls import include, path

from .views import SignUpView, home

urlpatterns = [
    path("", home, name="home"),
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/", include("django.contrib.auth.urls")),
]
