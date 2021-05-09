from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from django_otp.admin import OTPAdminSite

from blog import views

# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    re_path(r"^$", views.HomePageView.as_view(), name="home"),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("martor/", include("martor.urls")),
]
