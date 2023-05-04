from .common import CartSerializer
from jwt_auth.serializers.common import UserSerializer
from products.serializers.common import ProductSerializer

class PopulatedCartSerializer(CartSerializer):
    owner = UserSerializer()
    product = ProductSerializer(many=True)