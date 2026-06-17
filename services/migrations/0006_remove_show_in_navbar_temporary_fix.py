"""
Migration: Remove show_in_navbar field to fix 500 error.

ISSUE: The show_in_navbar field was added in migration 0004 but may not have
been applied on the Render server, causing database/model mismatch when trying
to add a Service from Django Admin.

SOLUTION: Removing this field from both model and database to restore functionality.
The field can be properly re-added later with proper migration management.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_add_doctors_gardeners_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='show_in_navbar',
        ),
    ]
