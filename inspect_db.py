import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    print('=== TABLES prefixed accounts_ ===')
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_name LIKE 'accounts_%' ORDER BY table_name")
    for row in cursor.fetchall():
        print(row[0])

    print('\n=== TABLES named User or auth_user ===')
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_name IN ('User','auth_user','accounts_user') ORDER BY table_name")
    for row in cursor.fetchall():
        print(row[0])

    def describe_table(table_name):
        cursor.execute("SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position", [table_name])
        print(f'\n=== COLUMNS for {table_name} ===')
        for col in cursor.fetchall():
            print(col)
        cursor.execute("SELECT tc.constraint_name, tc.constraint_type, kcu.column_name, ccu.table_name, ccu.column_name FROM information_schema.table_constraints tc JOIN information_schema.key_column_usage kcu ON tc.constraint_name=kcu.constraint_name JOIN information_schema.constraint_column_usage ccu ON ccu.constraint_name=tc.constraint_name WHERE tc.table_schema='public' AND tc.table_name=%s AND tc.constraint_type='FOREIGN KEY'", [table_name])
        print(f'\n=== FKs for {table_name} ===')
        for fk in cursor.fetchall():
            print(fk)

    for t in ['accounts_user', 'User', 'auth_user', 'accounts_userprofile']:
        cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name=%s)", [t])
        exists = cursor.fetchone()[0]
        print(f'{t} exists: {exists}')
        if exists:
            describe_table(t)

    print('\n=== django_migrations records for accounts ===')
    cursor.execute("SELECT id, name, applied FROM django_migrations WHERE app='accounts' ORDER BY applied")
    for row in cursor.fetchall():
        print(row)

    print('\n=== accounts_userprofile sample rows ===')
    try:
        cursor.execute('SELECT id, user_id, phone, address, city, state, pincode, user_type FROM accounts_userprofile LIMIT 20')
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print('accounts_userprofile SELECT failed:', e)

    print('\n=== auth_user count ===')
    try:
        cursor.execute('SELECT count(*) FROM auth_user')
        print(cursor.fetchone()[0])
    except Exception as e:
        print('auth_user count failed:', e)

    print('\n=== User count ===')
    try:
        cursor.execute('SELECT count(*) FROM "User"')
        print(cursor.fetchone()[0])
    except Exception as e:
        print('User count failed:', e)
