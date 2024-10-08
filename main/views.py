from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from main.models import Product
from main.forms import ProductEntryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Basket
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Basket
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


# Create your views here.

@login_required(login_url='/login')
def show_main(request): 

    context = {
        'name': 'MUHAMMAD DZIKRI ILMANSYAH',
        'class': 'PBP C',
        'uname' : request.user.username,

        'last_login' : request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    if request.method == 'POST':
        form = ProductEntryForm(request.POST, request.FILES)  # Add request.FILES to handle image upload
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')
    else:
        form = ProductEntryForm()

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    
    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductEntryForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return JsonResponse({'status': 'success'})

def basket_view(request):
    # Get all basket items for the logged-in user
    basket_items = Basket.objects.filter(user=request.user)

    # Calculate total price of all items in the basket
    total_price = sum(item.get_total_price() for item in basket_items)

    context = {
        'basket_items': basket_items,
        'total_price': total_price,
    }
    return render(request, 'basket.html', context)

@require_POST
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    basket_item, created = Basket.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        basket_item.quantity += quantity
    else:
        basket_item.quantity = quantity
    
    basket_item.save()
    return JsonResponse({'status': 'success'})

def remove_from_basket(request, product_id):
    # Get the basket item for the current user and product
    basket_item = get_object_or_404(Basket, user=request.user, product__id=product_id)

    if request.method == "POST":
        # Get the quantity to remove from the form
        quantity_to_remove = int(request.POST.get('quantity', 1))

        # If quantity after removal is less than or equal to 0, remove the product from the basket
        if basket_item.quantity - quantity_to_remove <= 0:
            basket_item.delete()
        else:
            # Otherwise, just reduce the quantity
            basket_item.quantity -= quantity_to_remove
            basket_item.save()

    return redirect('main:basket')

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    user = request.user
    image = request.FILES.get("image")

    new_product = Product(
        name=name,
        price=price,
        description=description,
        image=image,
        user=user
    )
    new_product.save()

    return JsonResponse({"status": "success", "message": "Product added successfully"}, status=201)

def get_product_json(request):
    products = Product.objects.filter(user=request.user)
    return JsonResponse(list(products.values()), safe=False)