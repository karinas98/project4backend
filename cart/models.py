from django.db import models

# Create your models here.
class Cart(models.Model):
    product = models.ManyToManyField(
        'products.Product',
        related_name='cart',
            )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='cart',
        on_delete=models.CASCADE,
        
    )
def __str__(self):
        return f"{self.product}"
