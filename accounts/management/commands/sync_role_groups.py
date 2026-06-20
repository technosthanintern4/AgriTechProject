from django.core.management.base import BaseCommand
from accounts.roles import create_roles_and_permissions


class Command(BaseCommand):
    help = 'Create role groups and assign permissions for the accounts roles.'

    def handle(self, *args, **options):
        create_roles_and_permissions()
        self.stdout.write(self.style.SUCCESS('Role groups and permissions synced successfully.'))
