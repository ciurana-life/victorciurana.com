from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import BlogPost, HomePageContent



class CsrfExemptView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CsrfExemptView, self).dispatch(request, *args, **kwargs)


class HomePageView(CsrfExemptView, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_content'] = HomePageContent.objects.first()
        context['blog_post'] = BlogPost.objects.last()
        return context


class BlogPostListView(CsrfExemptView, ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'


class BlogPostDetailView(CsrfExemptView, DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
