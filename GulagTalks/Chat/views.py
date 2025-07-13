from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ChatmessageCreateForm
from .models import GroupChats

# Create your views here.

@login_required
def chat_view(request):
    chat_group = get_object_or_404(GroupChats, group_name="Public-Chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form=ChatmessageCreateForm()
    
    if request.htmx:
        form=ChatmessageCreateForm(request.POST)
        if form.isvalid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context ={
                'message': message,
                'user': request.user
            }
            return render(request,'chat/partials/chat_message_p.html',context)
        
    return render(request,"chatPage.html"),{'chat_messages':chat_messages, 'form': form}