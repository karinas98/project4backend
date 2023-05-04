from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.conf import settings
from .models  import User
import jwt
from .serializers.common import UserSerializer

# User = get_user_model()

 
class UserView(APIView):

    def get_user_model(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail="Can't find a product with this Primary Key")
        
    def post(self, _request, pk):
        user = self.get_user_model(pk=pk)
        serialized_owner = UserSerializer(user)
        return Response(serialized_owner.data, status=status.HTTP_200_OK)



class RegisterView(APIView):
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': "registration successful"}, status=status.HTTP_201_CREATED)
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied(detail="No user found with that email. Please Register")
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail="Invalid Credentials")
        
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            {'sub': user_to_login.id, 'exp':int(dt.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return Response({'token': token, 'message': f"Welcome Back {user_to_login.username}"})
  