from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as check_login


def autorization(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "Autorization.html")

def registration(request):
    return render(request, "registration.html")

def registration_entrails(request):
    data = {}
    print("РАБОТАЕТ ЭНТРЕЙЛС")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    if len(username) <= 3:
        data["error"] = "Пользователь подходит под стандарты"
        return render(request, "registration.html", data)
    if not len(password) <= 5:
        data["error"] = "Пользователь подходит под стандарты"
        return render(request, "registration.html", data)

def puzzle_function(request):
    data = {}
    print("РАБОТАЕТ")
    login = request.POST.get("login", "")
    password = request.POST.get("password", "")
    name = request.POST.get("name", "")
    surname = request.POST.get("surname", "")
    user_parametres = User(username=login, first_name=name, last_name=surname, ) #преподаватель обещал показать хэширование пароля здесь!
    user_parametres.save()
    user_parametres.set_password(password)
    user_parametres.save()
    return redirect("/")

def puzzle_dunction(request):
    print("Отчет о попытке авторизации")
    data = {}
    login = request.POST.get("login", "")
    password = request.POST.get("password", "")
    print("\n", login, password, "\n", "TEST")
    user = authenticate(username=login, password=password)
    if user is not None:
        check_login(request, user)
    else:
        print("Пользователь не в этом пространстве")
        helicopter = {}
        helicopter["error"] = "Пользователь не найден"
        return render(request, "Autorization.html", helicopter)
    return redirect("/")








