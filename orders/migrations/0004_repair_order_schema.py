from django.db import migrations


def repair_order_columns(apps, schema_editor):
    table_name = 'orders_order'
    existing_tables = schema_editor.connection.introspection.table_names()

    if table_name not in existing_tables:
        return

    with schema_editor.connection.cursor() as cursor:
        existing_columns = {
            column.name
            for column in schema_editor.connection.introspection.get_table_description(
                cursor,
                table_name,
            )
        }

        if schema_editor.connection.vendor == 'postgresql':
            if 'user_id' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN user_id bigint NULL')
            if 'full_name' not in existing_columns:
                cursor.execute("ALTER TABLE orders_order ADD COLUMN full_name varchar(200) NOT NULL DEFAULT ''")
            if 'city' not in existing_columns:
                cursor.execute("ALTER TABLE orders_order ADD COLUMN city varchar(100) NOT NULL DEFAULT ''")
            if 'is_completed' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN is_completed boolean NOT NULL DEFAULT false')
            if 'is_cancelled' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN is_cancelled boolean NOT NULL DEFAULT false')

            cursor.execute(
                """
                UPDATE orders_order
                SET full_name = COALESCE(NULLIF(full_name, ''), name, '')
                WHERE full_name IS NULL OR full_name = ''
                """
            )

            if 'farmer_id' in existing_columns:
                cursor.execute(
                    """
                    UPDATE orders_order
                    SET user_id = farmer_id
                    WHERE user_id IS NULL
                      AND farmer_id IS NOT NULL
                      AND EXISTS (
                          SELECT 1
                          FROM accounts_user
                          WHERE accounts_user.id = orders_order.farmer_id
                      )
                    """
                )

        else:
            if 'user_id' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN user_id bigint NULL')
            if 'full_name' not in existing_columns:
                cursor.execute("ALTER TABLE orders_order ADD COLUMN full_name varchar(200) DEFAULT ''")
            if 'city' not in existing_columns:
                cursor.execute("ALTER TABLE orders_order ADD COLUMN city varchar(100) DEFAULT ''")
            if 'is_completed' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN is_completed bool DEFAULT 0')
            if 'is_cancelled' not in existing_columns:
                cursor.execute('ALTER TABLE orders_order ADD COLUMN is_cancelled bool DEFAULT 0')


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.RunPython(
            repair_order_columns,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
