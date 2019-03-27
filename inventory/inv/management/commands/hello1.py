from django.core.management.base import BaseCommand

class Command(BaseCommand):
help = "Say Hello World!"
	
def handle(self, *args, **options):
	self.stdout.write("Hello World")
