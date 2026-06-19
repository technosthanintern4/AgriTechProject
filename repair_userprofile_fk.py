import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT tc.constraint_name, ccu.table_name "
        "FROM information_schema.table_constraints tc "
        "JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name "
        "JOIN information_schema.constraint_column_usage ccu ON ccu.constraint_name = tc.constraint_name "
        "WHERE tc.table_name = 'accounts_userprofile' "
        "AND tc.constraint_type = 'FOREIGN KEY' "
        "AND kcu.column_name = 'user_id'"
    )
    rows = cursor.fetchall()
    if not rows:
        print('No foreign key constraints found on accounts_userprofile.user_id')
        raise SystemExit(1)

    auth_fk = None
    for constraint_name, referenced_table in rows:
        if referenced_table == 'auth_user':
            auth_fk = constraint_name
            break

    if not auth_fk:
        print('No auth_user foreign key constraint found; nothing to change.')
        raise SystemExit(0)

    print(f'Dropping constraint {auth_fk}')
    cursor.execute(f'ALTER TABLE accounts_userprofile DROP CONSTRAINT "{auth_fk}"')
    print('Adding foreign key to accounts_user')
    cursor.execute(
        "ALTER TABLE accounts_userprofile "
        "ADD CONSTRAINT accounts_userprofile_user_id_fk_accounts_user_id "
        "FOREIGN KEY (user_id) REFERENCES accounts_user (id) DEFERRABLE INITIALLY DEFERRED"
    )

print('Repair complete.')
