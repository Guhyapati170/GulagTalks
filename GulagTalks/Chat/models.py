from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GroupChats(models.Model):
    group_name=models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.group_name
    
    class Meta:
        verbose_name_plural=("Groups")
    
class GC_messages(models.Model):
    group = models.ForeignKey(GroupChats, related_name='Messages', on_delete=models.CASCADE)
    owner = models.ForeignKey(User,related_name='Author', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    body=models.CharField(max_length=300, default='Hey!') 
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.username} : {self.description}"
    
    class Meta:
        ordering=['-created']
        verbose_name_plural=("Group Messages")
        
# class ChatmessageCreateForm(models.Model):
#     class Meta:
#         model = GC_messages
#         fields = ['body']
#         widgets = {
#             'body': models.TextField(attrs={'placeholder':'Add message ...','class': 'p-4 text-black', 'maxlength': '300', 'autofocus':True})
#         }
        