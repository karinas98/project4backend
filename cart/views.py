from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers.common import CartSerializer
from .serializers.populated import PopulatedCartSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Cart

# Create your views here.
class CartListView(APIView):
    # permission_classes = (IsAuthenticated, )
    def get(self, _request):
        cart = Cart.objects.all()
        serialized_cart_items = CartSerializer(cart, many=True)
        return Response(serialized_cart_items.data, status=status.HTTP_200_OK)

#Add to Cart
    def post(self, request):
        request.data['owner'] = request.user.id
        cart_to_create = CartSerializer(data=request.data)

        try:
            cart_to_create.is_valid()
            cart_to_create.save()
            return Response(cart_to_create.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response("Unprocessible Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

class CartDetailView(APIView):
 
    def get_cart(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise NotFound(detail="Can't find a product with this Primary Key")

    def put(self, request, pk):
        request.data['owner'] = request.user.id
        cart_to_edit = self.get_cart(pk=pk)
        updated_cart = CartSerializer(cart_to_edit, data=request.data)
        try:
            updated_cart.is_valid()
            updated_cart.save()
            return Response(updated_cart.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            Response({"detail": "Unprocessible Entity"},
                     status=status.HTTP_422_UNPROCESSABLE_ENTITY)
