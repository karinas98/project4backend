from .common import ProductSerializer
from categories.serializers.common import CategorySerializer
from reviews.serializers.populated import PopulatedReviewSerializer
from jwt_auth.serializers.common import UserSerializer
# add all app serializers needed


class PopulatedProductSerializer(ProductSerializer):
    category = CategorySerializer(many=True)
    reviews = PopulatedReviewSerializer(many=True)
    owner = UserSerializer()
