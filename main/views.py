from django.shortcuts import render

# Create your views here.
def show_product(request):
    context = {
        'name' : 'Desmond Regamaster Evo II Forged Alloy Wheel',
        'price' : '25.000.000',
        'description' : '19x9 ET45 5x100 Almighty Grey',
        'image' : 'https://www.torque-gt.co.uk/media/catalog/product/r/e/regamaster_evo_2_almighty_grey_1_1.png?width=800&height=800&store=default&image-type=image'
    }
    return render(request, 'main.html', context)

