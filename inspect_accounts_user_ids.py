import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('SELECT id, email, username FROM auth_user ORDER BY id')
    auth_users = cursor.fetchall()
    cursor.execute('SELECT id, email, username FROM accounts_user ORDER BY id')
    accounts_users = cursor.fetchall()

print('auth_user ids:', [row[0] for row in auth_users])
print('accounts_user ids:', [row[0] for row in accounts_users])
print('missing ids from accounts_user:', [row[0] for row in auth_users if row[0] not in {a[0] for a in accounts_users}])
print('\naccounts_user rows:')
for row in accounts_users:
    print(row)
print('\nauth_user duplicates:')
from collections import Counter
emails = [row[1] for row in auth_users]
for email, count in Counter(emails).items():
    if count > 1:
        print(email, count)
