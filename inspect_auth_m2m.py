import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    print('=== auth_user_groups ===')
    cursor.execute('SELECT user_id, group_id FROM auth_user_groups ORDER BY user_id, group_id')
    for row in cursor.fetchall():
        print(row)
    print('\n=== auth_user_user_permissions ===')
    cursor.execute('SELECT user_id, permission_id FROM auth_user_user_permissions ORDER BY user_id, permission_id')
    for row in cursor.fetchall():
        print(row)
