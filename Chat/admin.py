from django.contrib import admin
from Chat.models import User, ChatRooms, Message

admin.site.register(User)
admin.site.register(ChatRooms)
admin.site.register(Message)
