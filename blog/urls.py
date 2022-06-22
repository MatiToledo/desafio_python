from django.urls import path

from blog import views

app_name='blog'
urlpatterns = [
   path('', views.index, name='Index'),
   path('my-blogs', views.myBlogs, name='MyBlogs'),
   path('create', views.createBlog, name='Create'),
   path('<int:blogId>', views.detailBlog, name='Detail'),
   path('edit/<int:blogId>', views.editBlog, name='Edit'),
   path('delete/<int:blogId>', views.deleteBlog, name="Delete"),
   path('all', views.allBlogs, name='All'),
]