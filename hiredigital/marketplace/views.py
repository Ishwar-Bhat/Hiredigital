from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace.models import Products
from marketplace.serializers import ProductCategorySerializer, ProductsSerializer


class ProductView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_detail.html'
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        if pk == 'new':
            product = {'pk': 'new'}
            serializer = ProductsSerializer()
        else:
            product = get_object_or_404(Products, pk=pk)
            serializer = ProductsSerializer(product)
        return Response({'serializer': serializer, 'product': product})

    def post(self, request, pk):
        if pk == 'new':
            product = None
        else:
            product = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(product, data=request.data, context={'user': request.user})
        if not serializer.is_valid():
            if product is None:
                product = {'pk': 'new'}
            return Response({'serializer': serializer, 'product': product})
        serializer.save()
        return Response({'serializer': serializer, 'product': serializer.instance})


@api_view(['GET'])
def get_products(req):
    product_list = ProductsSerializer(Products.objects.all(), many=True)
    return render(req, 'products.html', {'product_list': product_list.data})


@api_view(['POST'])
def add_bulk_products(req):
    data = req.data

    product_category_ids = dict()

    error_items = list()

    for item in data:
        item_data = dict()
        item_data['product_id'] = item['productId']
        item_data['product_name'] = item['productName']
        item_data['product_image'] = item['productImage']
        item_data['product_price'] = item['productPrice']
        item_data['selling_price'] = item['salePrice']

        if not item['productCategory'] in product_category_ids:
            new_category = ProductCategorySerializer(data={'category_name': item['productCategory']})
            if new_category.is_valid():
                nc = new_category.save()
                product_category_ids[nc.category_name] = nc.id
            else:
                error_items.append(item)
                continue

        item_data['product_category'] = product_category_ids[item['productCategory']]

        if item['productStock']:
            item_data['product_stock'] = 1

        item_data['created_by'] = 2

        new_item = ProductsSerializer(data=item_data)
        if new_item.is_valid():
            new_item.save()
        else:
            error_items.append(item)

    return JsonResponse(data=error_items, safe=False)
