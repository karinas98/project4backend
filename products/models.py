from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=1000)
    img_url = models.CharField(max_length=500)
    category = models.ManyToManyField(
        'categories.Category', related_name='products')
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='products',
        on_delete=models.CASCADE
    )


    # this is only to make it readable inside admin app
    def __str__(self):
        return f"{self.title} - {self.price}"

    



