import random

from django.core.management.base import BaseCommand
from faker import Faker
from points.models import PointOfInterest


class Command(BaseCommand):
    help = "Populates the PointOfInterest model with 500 random objects"

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ["restaurant", "mosque", "park", "museum", "hotel"]
        pois = []

        self.stdout.write("Generating fake data...")
        for _ in range(500):
            poi = PointOfInterest(
                name=fake.company(),
                description=fake.text(max_nb_chars=200),
                latitude=random.uniform(-90.0, 90.0),
                longitude=random.uniform(-180.0, 180.0),
                category=random.choice(categories),
            )
            pois.append(poi)

        PointOfInterest.objects.bulk_create(pois)
        self.stdout.write(self.style.SUCCESS("Successfully added 500 POIs."))
