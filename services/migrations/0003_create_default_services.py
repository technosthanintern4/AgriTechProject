from django.db import migrations


def create_default_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    Service.objects.update_or_create(
        slug='contract-gardening',
        defaults={
            'title': 'Contract Gardening',
            'description': 'Long-term gardening support for maintenance, landscaping, and plant care contracts tailored to your home or business.',
            'is_active': True,
        }
    )
    Service.objects.update_or_create(
        slug='animal-wellness-pets-care',
        defaults={
            'title': 'Animal Wellness / Pets Care',
            'description': 'Specialized wellness services for pets and small animals, including nutrition advice, hygiene support, and care consultation.',
            'is_active': True,
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_add_default_services'),
    ]

    operations = [
        migrations.RunPython(create_default_services),
    ]
