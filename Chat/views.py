from django.shortcuts import render, redirect
from django.http import HttpResponse
from Chat.models import User, ChatRooms, Message
import templates

def main(request):
	return render(request, 'main.html')

def login_check(request):
    if 'username' in request.POST:
        if len(request.POST['username']) == 0:
            return HttpResponse('닉네임을 입력하세요')
        else:
            input_name = request.POST['username']
    else:
        return HttpResponse('닉네임을 입력하세요2')

    try:
        user = User.objects.get(Username=input_name)
        request.session['username'] = input_name
        return redirect('/chat/')
    except:
        return HttpResponse('닉네임이 존재하지 않습니다')

def register(request):
    return render(request, 'register.html')

def register_check(request):
    if 'username' in request.POST:
        if len(request.POST['username']) == 0:
            return HttpResponse('닉네임을 입력하세요')
        else:
            user_name = request.POST['username']
    else:
        return HttpResponse('닉네임을 입력하세요2')

    try:
        user_check = User.objects.get(Username=user_name)
        return HttpResponse('닉네임 중복')
    except:
    
        if 'password' in request.POST:
            if len(request.POST['password']) == 0:
                return HttpResponse('비밀번호를 입력하세요')
            else:
                user_password = request.POST['password']
        else:
            return HttpResponse('비밀번호를 입력하세요')

        try:
            new_user = User(Username=user_name, Password=user_password)
            new_user.save()
            return HttpResponse('아이디가 생성되었습니다')
        except:
            return HttpResponse('아이디 저장 오류')
        return HttpResponse('알 수 없는 에러')

def chat_view(request):
    username = request.session['username']
    chattingRoom = ChatRooms.objects.all()
    
    return render(request, 'chat_view.html', {
            "username": username,
            "ChatRooms": chattingRoom,
    })

def room_view(request, room_id=None):
    username = request.session['username']
    messages = Message.objects.filter(ChatRooms=room_id)
    return render(request, 'room_view.html', {
            "room_id": room_id,
            "username": username,
            "messages": messages,
    })

def send(request):
    if 'message' in request.POST:
        if len(request.POST['message']) == 0:
            return HttpResponse('메세지를 입력하세요')
        else:
            content = request.POST['message']
    else:
        return HttpResponse('메세지를 입력하세요')

    username = request.session['username']
    user = User.objects.get(Username=username)

    room_id = request.POST['room_id']
    room = ChatRooms.objects.get(id=room_id)

    try:
        new_message = Message(Username=user,ChatRooms=room,Content=content)
        new_message.save()
        return redirect('/rooms/'+room_id+'/')
    except:
        return HttpResponse('메세지 저장 에러')

