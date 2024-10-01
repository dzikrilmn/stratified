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


# Create your views here.

@login_required(login_url='/login')
def show_main(request): 
    product_entry = Product.objects.filter(user=request.user)
    context = {
        'name': 'MUHAMMAD DZIKRI ILMANSYAH',
        'class': 'PBP C',
        'uname' : request.user.username,
        'product_entry' : product_entry,
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
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
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
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry berdasarkan id
    mood = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    mood = Product.objects.get(pk = id)
    # Hapus mood
    mood.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

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

def add_to_basket(request, product_id):
    # Get the product to be added to the basket
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        # Get the quantity from the form
        quantity = int(request.POST.get('quantity', 1))

        # Check if the product is already in the user's basket
        basket_item, created = Basket.objects.get_or_create(user=request.user, product=product)

        # If the product already exists in the basket, update the quantity
        if not created:
            basket_item.quantity += quantity
        else:
            basket_item.quantity = quantity
        
        basket_item.save()
        messages.success(request, 'Product added to the basket!')

        return redirect('main:show_main')

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