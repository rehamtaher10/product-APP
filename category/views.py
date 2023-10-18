from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse
from category.models import Category

# Create your views here.


# def categoryHome(request):
#     return render(request, 'category/categoryHome.html')

def categoriesHome(request):
    categories=Category.objects.all()
    return render(request, 'category/categoryHome.html',context={"categories":categories})

def details(request, id):
    category= get_object_or_404(Category,pk=id)
    # products=category.product_set.all()
    return render(request,'category/categoryDetails.html',context={"category":category })

def delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    url=reverse('category.home')
    return redirect(url)