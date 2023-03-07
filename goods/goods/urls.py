from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    # path('orders/', include('orders.urls', namespace=orders)),
    # path('auth/', include('users.urls', namespace=users)),
    path('', include('shop.urls', namespace='shop')),
]
