from django.urls import path
from . import views


urlpatterns = [
    path('', views.customer, name='customer'),
    path('home/', views.home, name='home'),
    path('logout/', views.customer, name='logout'),
    #path('members/', views.members, name='members'),
    #path('details/<int:id>/', views.details, name='details'),
]