from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from blog import views



urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
]
