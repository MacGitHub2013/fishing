from django.urls import path
from .views import(
    FishListView,
    FishSearchView,
    FishDetailsView,
    FishCreateView,
    FishUpdateView,
    FishDeleteView
)


urlpatterns = [
    path('',FishListView.as_view(),name="fish-list"),
    path ('create',FishCreateView.as_view(), name="fish-create"),
    path('<int:pk>/', FishDetailsView.as_view(),name='fish'),
     path('<int:pk>/update', FishUpdateView.as_view(),name='fish-update'),
     path('<int:pk>/delete', FishDeleteView.as_view(), name='fish-delete'),
    path('<slug:key>/', FishSearchView.as_view(), name="fish-details"),
    
    #path('', BrekishWaterFishListView.as_view())
]