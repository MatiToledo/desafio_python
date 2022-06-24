from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def index(request):
  featuredBlogs = Blog.objects.all()[1:4].values()
  return render(request, 'home/index.html',{"featuredBlogs": featuredBlogs} )

