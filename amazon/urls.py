from django.urls import path ,include
from amazon.views import  amazonHome,contactUs,aboutUs,details,delete,searchResult,createForm,editForm

urlpatterns =[
     path('',amazonHome,name='amazon.home'),
     # path('',listt,name='amazon.home'),
     path('details/<int:id>',details , name='product.details'),
     path('contactUs/',contactUs , name='amazon.contactUs'),
     path('aboutUs/',aboutUs , name='amazon.aboutUs'),
     path('<int:id>',delete,name='product.delete'),
     path('search/',searchResult,name='amazon.result'),
     path('forms/create',createForm, name='amazon.create' ),
     path('<int:id>/forms/edit', editForm, name='amazon.editform'),
     # path('edit/<int:id>',edit, name='product.edit' ),
     path('api/', include('amazon.api.urls'))
     

]