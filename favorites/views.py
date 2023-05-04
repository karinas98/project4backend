from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers.common import FavoriteSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Favorites

# Create your views here.
class FavoriteListView(APIView):
    # permission_classes = (IsAuthenticated, )
    def get(self, _request):
        favorite = Favorites.objects.all()
        serialized_favorite_items = FavoriteSerializer(favorite, many=True)
        return Response(serialized_favorite_items.data, status=status.HTTP_200_OK)

#Add to Cart
    def post(self, request):
        request.data['owner'] = request.user.id
        favorite_to_create = FavoriteSerializer(data=request.data)

        try:
            favorite_to_create.is_valid()
            favorite_to_create.save()
            return Response(favorite_to_create.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response("Unprocessible Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class FavoriteDetailView(APIView):
    def delete(self, request, pk):
        try:
            favorite_to_delete = Favorites.objects.get(pk=pk)
            if favorite_to_delete.owner != request.users:
                raise PermissionDenied()
            favorite_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorites.DoesNotExist:
            raise NotFound(detail="Item not found")