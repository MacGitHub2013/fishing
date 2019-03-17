from django.urls import path
from .views import (
    
    BCreateUserView,
    logout_view
)

#from user.views import create_user_view

urlpatterns = [

    #path('logout',logout_view, name = 'logout'),
    #path('signup',create_user_view, name='signup')
    path('signup',BCreateUserView.as_view(), name='signup')
    

]