from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from main.views import show_product
from main.views import show_main
from main.views import show_main, create_product_entry
from main.views import show_main, create_product_entry, show_xml
from main.views import show_main, create_product_entry, show_xml, show_json
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product, add_product_ajax
from django.urls import path
from . import views



app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', views.edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('basket/', views.basket_view, name='basket'),
    path('add-to-basket/<uuid:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove-from-basket/<uuid:product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('delete-product/<uuid:id>/', views.delete_product, name='delete_product'),
    path('add-to-basket/<uuid:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('get-product-json/', views.get_product_json, name='get_product_json'),
]