from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
  user_one = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user_one')
  user_two = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user_two')
  
  def __str__(self):
        return f'{self.user_one} and {self.user_two} '

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(max_length=500) # what length you want