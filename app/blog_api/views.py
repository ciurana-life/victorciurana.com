from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from app.blog.models import BlogPost, HomePageContent

from .serializers import BlogPostSerializer, HomePageContentSerializer


class HomePageContentView(generics.RetrieveAPIView):
    """
    Retrieve last HomePageContent object or empty string
    """

    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer

    def get_object(self):
        return self.queryset.last()


class BlogPostViewSet(viewsets.ViewSet):
    """
    Lists or retrievews BlogPost objects.
    """

    @method_decorator(cache_page(60 * 60 * 24, key_prefix="blog"))
    def list(self, request: any) -> Response:
        queryset = (
            BlogPost.objects.all()
            .values("id", "title", "created_at")
            .order_by("-created_at")
        )
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60 * 24, key_prefix="blog"))
    def retrieve(self, request: any, pk: int = None) -> Response:
        queryset = BlogPost.objects.all()
        blogpost = get_object_or_404(queryset, pk=pk)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)
