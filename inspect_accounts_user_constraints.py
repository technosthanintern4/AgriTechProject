import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')
django.setup()
from django.db import connection

with connection.cursor() as cur:
    cur.execute("SELECT constraint_name, constraint_type FROM information_schema.table_constraints WHERE table_name='accounts_user'")
    print('constraints:', cur.fetchall())
    cur.execute("SELECT indexname, indexdef FROM pg_indexes WHERE tablename='accounts_user'")
    print('indexes:', cur.fetchall())
    cur.execute("SELECT indexname, indexdef FROM pg_indexes WHERE tablename='accounts_user_groups'")
    print('accounts_user_groups indexes:', cur.fetchall())
    cur.execute("SELECT indexname, indexdef FROM pg_indexes WHERE tablename='accounts_user_user_permissions'")
    print('accounts_user_user_permissions indexes:', cur.fetchall())
    cur.execute("SELECT email, COUNT(*) FROM auth_user GROUP BY email HAVING COUNT(*) > 1")
    print('dup emails:', cur.fetchall())
