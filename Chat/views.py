from django.shortcuts import render
from django.http import HttpResponse
from Chat.models import User, ChatRooms, Message
import templates

def main(request):
	return render(request, 'main.html')

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
