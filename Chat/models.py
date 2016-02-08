from django.db import models

class User(models.Model):
	Username = models.CharField(max_length=30, null=False)
	Created = models.DateTimeField(auto_now_add=True)
	Password = models.CharField(max_length=32, null=False)

class ChatRooms(models.Model):
	Roomname = models.CharField(max_length=30, null=False)
	Max = models.PositiveSmallIntegerField(default=50, null=True)
	Current = models.PositiveSmallIntegerField(default=0, null=True)

class Message(models.Model):
	Username = models.ForeignKey(User)
	ChatRooms = models.ForeignKey(ChatRooms)
	Content = models.TextField(null=False)
	Created = models.DateTimeField(auto_now_add=True)
