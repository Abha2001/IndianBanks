from django.urls import path,include
from . import views

urlpatterns = [
    path('getbranches/', views.SearchBranchesList.as_view(),name='getbranches'),
    path('',views.index,name="index"),
]
