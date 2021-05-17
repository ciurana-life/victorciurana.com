from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from django_otp.admin import OTPAdminSite

from app.blog import views
from app.config.settings import DEBUG

if not DEBUG:
    admin.site.__class__ = OTPAdminSite

urlpatterns = [
    re_path(r"^$", views.HomePageView.as_view(), name="home"),
    path("blog/", include("app.blog.urls")),
    path("blog_api/", include("app.blog_api.urls")),
    path("admin/", admin.site.urls),
    path("martor/", include("martor.urls")),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
]
