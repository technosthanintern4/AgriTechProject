# Generated migration to handle user_type column

from django.db import migrations, models


def make_user_type_nullable(apps, schema_editor):
    """Make user_type column nullable"""
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("ALTER TABLE accounts_userprofile ALTER COLUMN user_type DROP NOT NULL;")


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_repair_userprofile_schema'),
    ]

    operations = [
        migrations.RunPython(
            make_user_type_nullable,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
