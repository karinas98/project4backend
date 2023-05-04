from django.db import models

# Create your models here.
class Favorites(models.Model):
     product = models.ForeignKey(
        'products.Product',
        related_name='favorites',
        on_delete=models.CASCADE,
            )
     owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='favorites',
        on_delete=models.CASCADE,
        
    )
    
def __str__(self):
        return f"{self.product}"
