from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from blog.models import Blog


class BlogForm(ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'subtitle', 'body', 'image', ]