from django.urls import path
from products.views import ProductView

app_name = 'products'

urlpatterns = [
    path('list/', ProductView.as_view(), name='product'),
]
