import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT tc.table_name, kcu.column_name, ccu.table_name AS fk_table, ccu.column_name AS fk_column "
        "FROM information_schema.table_constraints tc "
        "JOIN information_schema.key_column_usage kcu ON tc.constraint_name=kcu.constraint_name "
        "JOIN information_schema.constraint_column_usage ccu ON ccu.constraint_name=tc.constraint_name "
        "WHERE tc.constraint_type='FOREIGN KEY' AND ccu.table_name='auth_user' "
        "ORDER BY tc.table_name"
    )
    for row in cursor.fetchall():
        print(row)
