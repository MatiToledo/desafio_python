from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=100)
  body = RichTextUploadingField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='blogs', null=True, blank=True)
  date = models.CharField(max_length=100)
  user_name = models.CharField(max_length=100, default=None)
  user_avatar = models.TextField(default=None)

  def __str__(self):
    return f'Titulo: {self.title}'