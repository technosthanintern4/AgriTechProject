import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('SELECT id, username, email, is_staff, is_superuser, is_active FROM auth_user ORDER BY id')
    rows = cursor.fetchall()
    print('auth_user records:')
    for row in rows:
        print(row)
    cursor.execute("SELECT email, COUNT(*) FROM auth_user GROUP BY email HAVING COUNT(*) > 1")
    print('\nduplicates:')
    for row in cursor.fetchall():
        print(row)
