from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "announcements/home.html")



def official(request):
    return render(request, "announcements/official.html")
