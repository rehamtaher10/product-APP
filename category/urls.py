from django.urls import path
from category.views import categoriesHome,details,delete

urlpatterns =[
     path('',categoriesHome,name='category.home'),
     path('details/<int:id>',details , name='category.details'),
     path('<int:id>',delete,name='category.delete'),
     
]