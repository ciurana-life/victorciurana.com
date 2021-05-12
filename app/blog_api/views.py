from rest_framework import generics

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


class BlogPostListView(generics.ListAPIView):
    """
    List all BlogPost objects, paginated (10)
    """

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveAPIView):
    """
    Retrieve single BlogPost object
    """

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
