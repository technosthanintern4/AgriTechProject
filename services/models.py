from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class ServiceCategory(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if hasattr(self, 'name') and getattr(self, 'slug', None) in (None, ''):
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while ServiceCategory.objects.filter(slug=slug).exclude(pk=getattr(self, 'pk', None)).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Service(models.Model):

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        null=True,
        blank=True
    )   

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    description = models.TextField()

    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['title']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    @classmethod
    def active_navbar_services(cls):
        return cls.objects.filter(
            is_active=True
        ).order_by('title')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if hasattr(self, 'title') and getattr(self, 'slug', None) in (None, ''):
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Service.objects.filter(slug=slug).exclude(pk=getattr(self, 'pk', None)).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)