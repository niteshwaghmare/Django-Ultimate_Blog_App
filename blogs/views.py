from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(*kwargs)
        blogs = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(blogs, self.paginate_by)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        context['blogs'] = blogs
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blogpost.html"
    context_object_name = 'blog'