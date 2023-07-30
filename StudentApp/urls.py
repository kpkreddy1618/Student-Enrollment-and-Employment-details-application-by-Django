from django.urls import path
from . import views

urlpatterns=[
    path('',views.menu),
    path('home',views.menu),
    path('reg',views.register),
    path('registered',views.existing),
    path('search',views.search),
    path('update',views.update),
    path('updaterecord',views.updateform),
    path('drop',views.dropout)
]