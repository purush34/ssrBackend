# from django.conf.urls import url
from django.urls import path, include
from ssrData import views

urlpatterns = [
    path('projects/', views.ssrApiView),
    path('projects/year/<int:year>/', views.ssrYear),
    path('projects/category/<str:category>/', views.ssrCategory),
    path('projects/year/', views.getYears),
    path('projects/category/', views.getCatories),
]