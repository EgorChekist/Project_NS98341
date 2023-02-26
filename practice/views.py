from django.shortcuts import render



# Create your views here.
def practice(request):
    data = {}
    word = "long"
    data["practice"] = [word]
    return render(request, "practice.html", data)

