from django.db import migrations


def add_missing_userprofile_columns(apps, schema_editor):
    table_name = 'accounts_userprofile'
    existing_tables = schema_editor.connection.introspection.table_names()

    if table_name not in existing_tables:
        return

    UserProfile = apps.get_model('accounts', 'UserProfile')
    existing_columns = {
        column.name
        for column in schema_editor.connection.introspection.get_table_description(
            schema_editor.connection.cursor(),
            table_name,
        )
    }

    for field_name in (
        'bio',
        'alternate_phone',
        'profile_image',
        'created_at',
        'updated_at',
    ):
        if field_name not in existing_columns:
            schema_editor.add_field(
                UserProfile,
                UserProfile._meta.get_field(field_name),
            )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_missing_userprofile_columns,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
