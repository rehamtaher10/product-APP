from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse
from amazon.models import Product
from category.models import Category
from amazon.form import createProductForm
from django.contrib.auth.decorators import login_required


# products = [
#     {"id":1, "name":"AirFryer", "image":"airF.png","price":3000, "Decritopn":"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", "stock": 20},
#     {"id":2, "name":"Coffe Maker", "image":"coffeM.png", "price":4000, "Decritopn":"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", "stock":40},
#     {"id":3, "name":"Microwave", "image":"microwave.png", "price":2000, "Decritopn":"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.","stock":0},
#     {"id":4, "name":"Toaster", "image":"toaster.png", "price":5000, "Decritopn":"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.","stock":0}
# ]


# def amazonHome(request):
#     return render(request, 'amazon/amazonHome.html',context={"products":products})

# def listt(request):
#     return HttpResponse(products)


# def details(request, id):
#     product = list(filter(lambda product:product['id']==id , products)  )
   

#     if product:
#         # print(products[0])
#         return render(request, 'amazon/productDetails.html',context={"product":product[0]})

#     return HttpResponse("Sorry target product profile not found ")

def contactUs(request):
    return render(request, 'amazon/contactUs.html')

def aboutUs(request):
    return render(request, 'amazon/aboutUs.html')

def amazonHome(request):
    products=Product.objects.all()
    return render(request, 'amazon/amazonHome.html',context={"products":products})

def details(request, id):
    
    product= get_object_or_404(Product,pk=id)
    return render(request,'amazon/productDetails.html',context={"product":product})

# def details(request, id):
#     category= get_object_or_404(Category,pk=id)
#     return render(request,'category/categoryDetails.html',context={"category":category})

def delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    url=reverse('amazon.home')
    return redirect(url)

def searchResult(request):
    query=request.GET.get('search')
    products=Product.objects.filter(name__istartswith=query)
    return render(request,'amazon/searchResult.html',{'products':products})

@login_required()
def createForm(request):
  form = createProductForm()
  if request.POST:
    form = createProductForm(request.POST, request.FILES)
    if form.is_valid():
      name = request.POST['name']
      description = request.POST['description']
      price = request.POST['price']
      stock = request.POST['stock']
      owner = request.user
      image = None
      if "image" in request.FILES:
        image = request.FILES['image']
      category = None
      if request.POST['category']:
        category = Category.objects.get(id=request.POST['category']) 
        product = Product.objects.create(name=name, description=description, price=price,owner=owner, stock=stock, image=image, category=category)
        url = reverse('amazon.home') 
        return redirect(url)
  return  render(request, 'amazon/forms/create.html', context={"form":form})

@login_required()
def editForm(request, id):
  product = get_object_or_404(Product, id=id,owner=request.user)
  form = createProductForm(instance=product)
  if request.POST:
    form = createProductForm(request.POST, request.FILES ,instance=product)
    if form.is_valid():
      product.name = request.POST['name']
      product.description = request.POST['description']
      product.price = request.POST['price']
      product.stock = request.POST['stock']
      product.image = None
      if "image" in request.FILES:
        product.image = request.FILES['image']
      product.category = None
      if request.POST['category']:
        product.category = Category.objects.get(id=request.POST['category']) 
      product.save()
      return redirect(product.get_detail_url())
  return render(request, 'amazon/forms/edit.html', {'form': form, 'product': product})







