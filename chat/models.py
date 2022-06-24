from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    participants = models.OneToOneField(User, related_name='chats', on_delete=models.CASCADE)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500) # what length you want