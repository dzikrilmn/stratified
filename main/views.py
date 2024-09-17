from django.shortcuts import render
from django.shortcuts import render, redirect 
from main.models import Product
from main.forms import ProductEntryForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request): 
    product_entry = Product.objects.all()
    context = {
        'uname': 'Muhammad Dzikri Ilmansyah',
        'uclass': 'PBP C',
        # 'name' : 'Desmond Regamaster Evo II Forged Alloy Wheel',
        # 'price' : '25.000.000',
        # 'description' : '19x9 ET45 5x100 Almighty Grey',
        'product_entry' : product_entry
    }

    return render(request, "main.html", context)


# def product_entry(request):
#     product_entry = Product.objects.all()
#     context = {
#         'name' : 'Desmond Regamaster Evo II Forged Alloy Wheel',
#         'price' : '25.000.000',
#         'description' : '19x9 ET45 5x100 Almighty Grey',
#     }
#     return render(request, 'product_entry.html', context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



