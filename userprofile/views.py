from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from . forms import ProfileChangeForm
from . models import UserProfile
from django.views.generic import DetailView
# Create your views here.

class ProfileChangeView(TemplateView):
    def get(self,request):
        userprofile = get_object_or_404(UserProfile, user_id = request.user.id)
        form = ProfileChangeForm(instance=userprofile)
        return render(request,'userprofile/profile_change_view.html',{'form':form})
    
    def post(self,request):
        userprofile = get_object_or_404(UserProfile, user_id = request.user.id)
        
        form = ProfileChangeForm(request.POST, instance=userprofile)
        form.instance.user = request.user
        
        if form.is_valid():
            instance = form.save()
        return render(request,'userprofile/profile_view.html',{'object':instance})


