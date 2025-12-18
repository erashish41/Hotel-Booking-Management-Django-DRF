from django.core.management.base import BaseCommand
from faker import Faker
import random

from hotel.models import (
    Destination, Facility, Hotel, Room, Review,
    HOTEL_TYPE, FACILITY_TYPE, ROOM_TYPE, AMENITIES
)
from user_auth.models import User


class Command(BaseCommand):
    help = "Seed fake data for hotel booking system"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS("Seeding data started"))

        # USERS
        users = []
        for _ in range(10):
            user, created = User.objects.get_or_create(
                username=fake.user_name(),
                defaults={
                    "email": fake.email(),
                }
            )
            user.set_password("password123")
            user.save()
            users.append(user)

        self.stdout.write(self.style.SUCCESS("Users created"))

        # DESTINATIONS
        destinations = []
        for _ in range(50):
            dest = Destination.objects.create(
                city=fake.city(),
                description=fake.text(max_nb_chars=150)
            )
            destinations.append(dest)

        self.stdout.write(self.style.SUCCESS("Destinations created"))

        # FACILITIES
        facilities = []
        for key, value in FACILITY_TYPE:
            facility, _ = Facility.objects.get_or_create(
                facility_type=key
            )
            facilities.append(facility)

        self.stdout.write(self.style.SUCCESS("Facilities created"))

        # HOTELS
        hotels = []
        for _ in range(20):
            hotel = Hotel.objects.create(
                name=fake.company(),
                address=fake.address(),
                hotel_type=random.choice(HOTEL_TYPE)[0],
                description=fake.text(),
                destination=random.choice(destinations),
                manager=random.choice(users),
                contact=fake.msisdn()[:10],
            )

            hotel.facilities.set(
                random.sample(facilities, k=random.randint(2, 5))
            )
            hotels.append(hotel)

        self.stdout.write(self.style.SUCCESS("Hotels created"))

        # ROOMS
        rooms = []
        for hotel in hotels:
            for i in range(random.randint(3, 6)):
                room = Room.objects.create(
                    room_type=random.choice(ROOM_TYPE)[0],
                    room_number=f"{random.randint(100,999)}",
                    description=fake.text(),
                    person=random.randint(1, 4),
                    hotel=hotel,
                    price=random.randint(2000, 15000),
                    amenities=random.choice(AMENITIES)[0],
                )
                rooms.append(room)

        self.stdout.write(self.style.SUCCESS("Rooms created"))

        # REVIEWS
        for _ in range(10):
            Review.objects.create(
                hotel=random.choice(hotels),
                user=random.choice(users),
                comment=fake.text(max_nb_chars=200),
                star_rating=round(random.uniform(1, 5), 1),
            )

        self.stdout.write(self.style.SUCCESS("Reviews created"))

        self.stdout.write(self.style.SUCCESS(" Fake data seeding completed!"))
