import datetime
from django.shortcuts import render
from django.contrib.auth import get_user_model
from chat.forms import MessageForm
from chat.models import Chat, Message
from user.models import Avatar
# Create your views here.

def getuserlist(request):
  users = get_user_model().objects.all().values()
  user_list = []
  for user in users:
    if user["username"] != "admin" and user["username"] != request.user.username:
      user_list.append(user)

  for user in user_list:
    try:
      avatar = Avatar.objects.get(user_id=user['id']).image.url
    except Avatar.DoesNotExist:
      avatar = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/271deea8-e28c-41a3-aaf5-2913f5f48be6/de7834s-6515bd40-8b2c-4dc6-a843-5ac1a95a8b55.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3MWRlZWE4LWUyOGMtNDFhMy1hYWY1LTI5MTNmNWY0OGJlNlwvZGU3ODM0cy02NTE1YmQ0MC04YjJjLTRkYzYtYTg0My01YWMxYTk1YThiNTUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.BopkDn1ptIwbmcKHdAOlYHyAOOACXW0Zfgbs0-6BY-E"
    user["avatar"] = avatar
  
  return user_list

def search(q, userlist):
  if q == "":
    result = userlist
  else:
    filtrada = []

    for user in userlist:
      if q in user["username"]:
        filtrada.append(user)
      
    result = filtrada
  
  return result

# ----------------------------------------------------------------------------------------------------

def index(request):
  users_list = getuserlist(request)
  
  if request.GET:
    q = request.GET['q']
    users_list = search(q, users_list)
      
    return render(request, 'chat/index.html', {"users": users_list} )

  return render(request, 'chat/index.html', {"users": users_list} )

# ----------------------------------------------------------------------------------------------------

def chat(request, username):
  users_list = getuserlist(request)

  user_to_chat = get_user_model().objects.get(username=username)
  try:
    avatar = Avatar.objects.get(user_id=user_to_chat.id).image.url
  except Avatar.DoesNotExist:
    avatar = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/271deea8-e28c-41a3-aaf5-2913f5f48be6/de7834s-6515bd40-8b2c-4dc6-a843-5ac1a95a8b55.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3MWRlZWE4LWUyOGMtNDFhMy1hYWY1LTI5MTNmNWY0OGJlNlwvZGU3ODM0cy02NTE1YmQ0MC04YjJjLTRkYzYtYTg0My01YWMxYTk1YThiNTUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.BopkDn1ptIwbmcKHdAOlYHyAOOACXW0Zfgbs0-6BY-E"
  
  try:
    my_avatar = Avatar.objects.get(user=request.user).image.url
  except Avatar.DoesNotExist:
    my_avatar = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/271deea8-e28c-41a3-aaf5-2913f5f48be6/de7834s-6515bd40-8b2c-4dc6-a843-5ac1a95a8b55.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3MWRlZWE4LWUyOGMtNDFhMy1hYWY1LTI5MTNmNWY0OGJlNlwvZGU3ODM0cy02NTE1YmQ0MC04YjJjLTRkYzYtYTg0My01YWMxYTk1YThiNTUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.BopkDn1ptIwbmcKHdAOlYHyAOOACXW0Zfgbs0-6BY-E"
  
  search_chat = Chat.objects.filter(user_one=request.user, user_two=user_to_chat) or Chat.objects.filter(user_two=request.user, user_one=user_to_chat)
  if not search_chat.exists():
    chat = Chat.objects.create(user_one=request.user, user_two=user_to_chat)
  else:
    chat = search_chat[0]

  messages = Message.objects.filter(chat=chat).values()
  form = MessageForm()

  if request.GET:
    q = request.GET['q']
    users_list = search(q, users_list)
      
    return render(request, 'chat/index.html', {"users": users_list, "user_to_chat": user_to_chat, "avatar":avatar, "messages": messages, "my_avatar": my_avatar} )
  
  if request.method == 'POST':
    form = MessageForm(request.POST)  
    if form.is_valid():
      info = form.cleaned_data
      time = datetime.datetime.now().strftime('%H:%M')
      message = Message(user=request.user, chat=chat, text=info['text'],time=time)
      message.save()
      return render(request, 'chat/index.html', {"users": users_list, "user_to_chat": user_to_chat, "avatar":avatar, "messages": messages, "my_avatar": my_avatar} )
  return render(request, 'chat/index.html', {"users": users_list, "user_to_chat": user_to_chat, "avatar":avatar, "messages": messages, "my_avatar": my_avatar} )
