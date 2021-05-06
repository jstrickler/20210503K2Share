from django.core.management.base import BaseCommand, CommandError

class SuperHeroBaseCommand(BaseCommand):
    help = "Demo command"

    def add_arguments(self, parser):
        parser.add_argument('demo_arg', type=int)

    def handle(self, *args, **options):
        self.stdout.write("HELLO" * options['demo_arg'] + '\n' )

