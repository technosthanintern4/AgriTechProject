from django.db import migrations


def delete_seeded_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    slugs = [
        'doctors-consultation',
        'gardeners',
        'contract-gardening',
        'animal-wellness-pets-care',
    ]
    Service.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_servicecategory_service_price_service_category'),
    ]

    operations = [
        migrations.RunPython(delete_seeded_services, reverse_code=migrations.RunPython.noop),
    ]
