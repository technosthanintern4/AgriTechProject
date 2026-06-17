from django.db import models
from cloudinary.models import CloudinaryField


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)

    # TEMPORARY
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    description = models.TextField()

    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name