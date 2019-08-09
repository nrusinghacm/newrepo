from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings
from django.contrib.auth import authenticate, login, logout
from .models import Chat

# Create your views here.
def Login(request):
    next= request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse('Account is not active at the moment')
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next':next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
def Home(request):
    c=Chat.objects.all()
    return render(request, "alpha/home.html", {'home':c})

def Post(request):
    if request.method == "POST":
        msg= request.POST.get('msgbox', None)
        c= Chat(user=request.user, message=msg)
        if msg!='':
            c.save()
        return JsonResponse({'msg':msg, 'user':c.user.username})
    else:
        return HttpResponse('request must be POST.')

def Message(request):
    c= Chat.objects.all()
    return render(request, 'alpha/message.html', {'chat':c})
