from django.core.management.base import BaseCommand
from core.models import SiteSettings


class Command(BaseCommand):
    help = 'Initialize default SiteSettings if not already created'

    def handle(self, *args, **options):
        if SiteSettings.objects.exists():
            self.stdout.write(
                self.style.WARNING('SiteSettings already exists. Skipping initialization.')
            )
            return

        try:
            SiteSettings.objects.create(
                enable_watermark=False,
                enable_background_video=False,
                watermark_position='bottom-right',
                watermark_opacity=0.8
            )
            self.stdout.write(
                self.style.SUCCESS('SiteSettings initialized successfully!')
            )
            self.stdout.write(
                self.style.SUCCESS('Please upload background image and watermark through Django admin.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error initializing SiteSettings: {str(e)}')
            )
