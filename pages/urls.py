from django.urls import path
from django.views.generic import TemplateView
app_name='pages'
urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='pages/about.html'), name = 'about' ),
    path('contact', TemplateView.as_view(template_name='pages/contact.html'),name = 'contact')
]