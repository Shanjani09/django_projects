from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('addProducts/',views.add_product,name='addProducts'),
    path('deleteProducts/',views.delete_products,name='deleteProducts'),
    path('carousel/',views.carousel_view,name='carousel'),
    path('grid/', views.grid_view, name='grid'),
]
