from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<slug>/', views.product_detail, name='product_detail'),
    path('<slug>/', views.product_list, name='product_list_by_category'),

]