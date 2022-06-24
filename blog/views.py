from django.shortcuts import get_object_or_404, redirect, render
import datetime
from blog.forms import BlogForm
from blog.models import Blog
from django.contrib.auth.models import User
from user.models import Avatar


# Create your views here.
def index(request):
  mainBlog = Blog.objects.filter(title='Como creamos esta página?').values()
  featuredBlogs = Blog.objects.all()[1:4].values()
  return render(request, 'blog/index.html', {"mainBlog": mainBlog[0], "featuredBlogs": featuredBlogs})

# ----------------------------------------------------------------------------------------------------

def myBlogs(request):
  myBlogs = Blog.objects.filter(user=request.user).values()
  return render(request, 'blog/my-blogs.html', {"myBlogs": myBlogs})

# ----------------------------------------------------------------------------------------------------

def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  
        if form.is_valid() and len(request.FILES) != 0:
            info = form.cleaned_data
            date = datetime.date.today().strftime("%B %d, %Y")
            user = request.user
            image = request.FILES['image']
            user_name = User.objects.get(username=request.user).get_full_name()
            avatar = Avatar.objects.filter(user=request.user.id)
            if len(avatar) == 0:
              user_avatar = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/271deea8-e28c-41a3-aaf5-2913f5f48be6/de7834s-6515bd40-8b2c-4dc6-a843-5ac1a95a8b55.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3MWRlZWE4LWUyOGMtNDFhMy1hYWY1LTI5MTNmNWY0OGJlNlwvZGU3ODM0cy02NTE1YmQ0MC04YjJjLTRkYzYtYTg0My01YWMxYTk1YThiNTUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.BopkDn1ptIwbmcKHdAOlYHyAOOACXW0Zfgbs0-6BY-E"
            else:
              user_avatar = avatar[0].image.url
            blog = Blog(title=info['title'],subtitle=info['subtitle'],body=info['body'],image=image,date=date,user=user,user_name=user_name,user_avatar=user_avatar)
            blog.save()
            return redirect("home:Index")
    form = BlogForm()
    return render(request, "blog/create.html", {"form": form})

# ----------------------------------------------------------------------------------------------------

def detailBlog(request, blogId = None):
  blog = Blog.objects.filter(id=blogId).values()
  return render(request, "blog/detail-blog.html",{"blog":blog[0]})

# ----------------------------------------------------------------------------------------------------

def editBlog(request, blogId = None):
  blog = Blog.objects.get(id=blogId)
  if request.user != blog.user:
    return render(request, "blog/no-access.html",)
  
  if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  
        if form.is_valid():
          info = form.cleaned_data
          blog.title = info["title"]
          blog.subtitle = info["subtitle"]
          blog.body = info["body"]
          blog.image = info["image"]
          blog.save()
          return redirect("home:Index")
  else:
    form = BlogForm(initial={"title": blog.title, "subtitle": blog.subtitle, "body": blog.body,})
  return render(request, "blog/edit.html", {"form": form})

# ----------------------------------------------------------------------------------------------------

def allBlogs(request):
  blogs = Blog.objects.all()
  return render(request, "blog/all.html", {"blogs": blogs})

# ----------------------------------------------------------------------------------------------------

def deleteBlog(request, blogId = None):
  blog = Blog.objects.get(id=blogId)
  if request.method == 'POST':
    blog.delete()
    return redirect("home:Index")

  return render(request, "blog/delete-blog.html", {"blog": blog})

