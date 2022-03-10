from django.core.management.base import BaseCommand

from movie.models import Movie


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        serializer's validate does not work when populating data.
        """

        if Movie.objects.filter(title="lord of ring").exists():
            print("already populated. remove all data")
            Movie.objects.all().delete()

        lord_of_ring = Movie.objects.create(
            title="lord of ring",
            description="hobbit!",
            release_date="2022-02-10",
            rating=12,
            us_gross=10,
            worldwide_gross=12,
        )
        lord_of_ring.save()

        print("finished populate")
