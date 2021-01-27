from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import Form_auth

def index(request):
# Функция index получает запрос от пользователя и выводит форму авторизации.
# Если пользователь существует и у него есть права доступа к ресурсу он на него перейдет.

    if request.POST:
        form = Form_auth(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            programm = request.POST.get('programms')

            user = authenticate(username = username.strip(),
                                password = password.strip()) 
                                
            if user == None:
                messages.success(request,'Пользователь не существует или пароль введен не правильно!')
                form = Form_auth()
                return render(request,'index.html',{'form':form}) 
            else:
                login(request,user)
                return redirect(programm)
    else:
        form = Form_auth()
        return render(request,'index.html',{'form':form}) 