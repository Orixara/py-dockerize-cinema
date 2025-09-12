from django.core.management.base import BaseCommand
from django.db import connections, DatabaseError
import time


class Command(BaseCommand):
    help_text = "Wait for database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                db_connection = connections["default"]
                db_connection.ensure_connection()
                break
            except DatabaseError:
                self.stdout.write("Try to connect again...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
