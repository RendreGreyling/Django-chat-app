from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message, Chat
# Create your views here.

@login_required
def chats(request):
    chats = Chat.objects.all()
    return render(request, 'chatapp/chats.html', {'chats': chats})

@login_required
def chat(request, slug):
    chat = Chat.objects.get(slug=slug)
    messages = Message.objects.filter(chat=chat)[0:25]
    return render(request, 'chatapp/chat.html', {'chat': chat, 'messages':messages})