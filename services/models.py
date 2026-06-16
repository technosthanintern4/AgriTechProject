from django.db import models
from cloudinary.models import CloudinaryField


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    show_in_navbar = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

    @classmethod
    def active_navbar_services(cls):
        return cls.objects.filter(
            is_active=True,
            show_in_navbar=True
        ).order_by('title')
