from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render (request,"pages/home.html")

def logout_view(request):
    return render(request, "registration/logout.html")