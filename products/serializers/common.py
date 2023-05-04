from rest_framework import serializers
from ..models import Product
from categories.serializers.common import CategorySerializer
from jwt_auth.serializers.common import UserSerializer
from reviews.serializers.populated import PopulatedReviewSerializer
from cart.serializers.common import CartSerializer



class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product #Model to Translate
        fields = '__all__' #Translate all fields

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    owner = UserSerializer()
    reviews = PopulatedReviewSerializer(many=True)
    # cart = CartSerializer(many=True)

    class Meta:
        model = Product #Model to Translate
        fields = '__all__' #Translate all fields