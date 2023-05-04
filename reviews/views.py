from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers.common import ReviewSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Review

# Create your views here.
class ReviewListView(APIView):
    # permission_classes = (IsAuthenticated, )
#CREATE Review
    def post(self, request):
        request.data['owner'] = request.user.id
        review_to_create = ReviewSerializer(data=request.data)

        try:
            review_to_create.is_valid()
            review_to_create.save()
            return Response(review_to_create.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response("Unprocessible Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class ReviewDetailView(APIView):
    def delete(self, request, pk):
        try:
            review_to_delete = Review.objects.get(pk=pk)
            if review_to_delete.owner != request.users:
                raise PermissionDenied()
            review_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            raise NotFound(detail="Review not found")