from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from .forms import BUserCreationForm


class BCreateUserView(TemplateView):
    def get(self,request):
        form = BUserCreationForm()
        context = {
            'form' : form
        }
        return render(request,"registration/signup.html",context)
    def post(self,request):
        form =BUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')



def logout_view(request):
    return render(request, "registration/logout.html")