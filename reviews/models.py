from django.db import models

# Create your models here.
class Review(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        'products.Product',
        related_name='reviews',
        on_delete=models.CASCADE,
        related_query_name='reviews'
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='reviews',
        on_delete=models.CASCADE,
        related_query_name='reviews'
    )


    def __str__(self):
        return f"{self.text}"