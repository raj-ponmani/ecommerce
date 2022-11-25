from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        queryset = Products.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
