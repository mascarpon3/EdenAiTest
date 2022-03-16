from rest_framework.views import APIView
from rest_framework.response import Response
from store.serializers import ProductSerializer, DiscountSerializer
from django.shortcuts import render, get_object_or_404
from store.models import Product


class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'store/index.html',
        context={"products": products}
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})
