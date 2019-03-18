from django.urls import path
from . views import ProfileChangeView
app_name="userprofile"
urlpatterns = [
 path('change_profile', ProfileChangeView.as_view(), name ="change_profile")

]