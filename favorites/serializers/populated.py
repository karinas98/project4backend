from .common import FavoriteSerializer
from jwt_auth.serializers.common import UserSerializer
from products.serializers.common import ProductSerializer

class PopulatedFavoriteSerializer(FavoriteSerializer):
    owner = UserSerializer()
    product = ProductSerializer(many=True)