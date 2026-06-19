import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()

from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
tables = [row[0] for row in cursor.fetchall()]

print('Database tables:')
for table in sorted(tables):
    print(f'  - {table}')

print(f'\nTotal tables: {len(tables)}')
print(f'Has accounts_user: {"accounts_user" in tables}')
print(f'Has accounts_userprofile: {"accounts_userprofile" in tables}')
