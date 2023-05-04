from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from .models import Product
from .serializers.common import ProductSerializer, CreateProductSerializer
from .serializers.populated import PopulatedProductSerializer


# Create your views here.
class ProductListView(APIView):  # endpoint to set /products
    # permission_classes = (IsAuthentiscated, ) #Cannot get or modify if not authenticated
    # GET DATA
    def get(self, _request):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)

    # CREATE DATA
    def post(self, request):
        request.data["owner"] = request.user.id
        product_to_add = CreateProductSerializer(data=request.data)
        print(request.data)
        try:
            product_to_add.is_valid()
            product_to_add.save()
            return Response(product_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {"detail": str(e)}
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # GET SINGLE PRODUCT
class ProductDetailView(APIView):
    # permission_classes = (IsAuthenticated, )
# GET the Individual Product

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound(detail="Can't find a product with this Primary Key")


# Get information of the Product
    def get(self, _request, pk):
        product = self.get_product(pk=pk)
        serialized_product = PopulatedProductSerializer(product)
        return Response(serialized_product.data, status=status.HTTP_200_OK)

    # MODIFY Product
    def put(self, request, pk):
        product_to_edit = self.get_product(pk=pk)
        updated_product = CreateProductSerializer(product_to_edit, data=request.data)
        try:
            updated_product.is_valid()
            updated_product.save()
            return Response(updated_product.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            Response({"detail": "Unprocessible Entity"},
                     status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # DELETE Product
    def delete(self, _request, pk):
        product_to_delete = self.get_product(pk=pk)
        product_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
