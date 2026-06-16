from django.db import migrations


def create_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    Service.objects.update_or_create(
        slug='doctors-consultation',
        defaults={
            'title': 'Doctors Consultation',
            'description': 'Expert plant doctors consultation for diagnosis, treatment and ongoing advice.',
            'is_active': True,
            'show_in_navbar': True,
        }
    )
    Service.objects.update_or_create(
        slug='gardeners',
        defaults={
            'title': 'Gardeners',
            'description': 'Professional gardening services including maintenance, landscaping and on-site labor.',
            'is_active': True,
            'show_in_navbar': True,
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_show_in_navbar'),
    ]

    operations = [
        migrations.RunPython(create_services),
    ]
