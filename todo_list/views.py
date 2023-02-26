from django.shortcuts import render, redirect
from todo_list.models import TODO

# Create your views here.
def todo_big_list(request):
    data = {}
    if request.user.is_authenticated:
        data["TODO"] = TODO.objects.filter(check_table=request.user)
    else:
        data["TODO"] = TODO.objects.filter(check_table=None)
    print(data)
    return render(request, "homepage.html", data)

def check_url_deleting(request, pk):
    print(pk, "text")
    TODO.objects.filter(id=pk).delete()
    return redirect("/")

def stick_stuff(request, pn):
    stick = TODO.objects.get(id=pn)
    stick.stick = not stick.stick
    stick.save(update_fields=["stick"])
    return redirect("/")

def puzzle_function(request):
    data = {}
    task = request.POST.get("task", "")
    priority = request.POST.get("priority", "")
    if request.user.is_authenticated:
        TODO.objects.create(text=task, priority=priority, check_table=request.user)
    else:
        TODO.objects.create(text=task, priority=priority)
    return redirect("/")