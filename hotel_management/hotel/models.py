from django.db import models
from utils.models import BaseMixin
from user_auth.models import User

# Create your models here.

HOTEL_TYPE = (
    ('hotel', 'Hotel'),
    ('apartment', 'Apartment'),
    ('resort', 'Resort'),
    ('villa', 'Villa',),
    ('cottage', 'Cottage'),
    ('hostel', 'Hostel'),
    ('suit', 'Suit'), 
)

FACILITY_TYPE = (
    ('wifi', 'Wi-Fi'),
    ('pool', 'Swimming Pool'),
    ('gym', 'Gym'),
    ('parking', 'Parking'),
    ('ac', 'Air Conditioning'),
    ('laundry', 'Laundry Service'),
    ('restaurant', 'Restaurant'),
    ('bar', 'Bar'),
    ('spa', 'Spa'),
    ('pet_friendly', 'Pet Friendly'),
    ('kids_play_area', 'Kids Play Area'),
    ('game_room', 'Game Room'),
    ('meeting_room', 'Meeting Room'),
)

ROOM_TYPE= (
    ('single', 'Single'),
    ('double', 'Double'),
    ('king', 'King'),
    ('deluxe', 'Deluxe')
)

AMENITIES = [
    ('ac', 'Air Conditioning'),
    ('wifi', 'Free WiFi'),
    ('minibar', 'Minibar'),
    ('tv', 'Smart TV with Streaming'),
    ('room_service', 'Room Service Available'),
    ('balcony', 'Private Balcony'),
    ('soundproof', 'Soundproof Windows'),
    ('safe', 'In-Room Safe'),
    ('desk', 'Desk & Workstation'),
    ('coffee', 'Coffee/Tea Maker'),
]

class Destination(BaseMixin):
    city = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.city
class Facility(BaseMixin):
    facility_type = models.CharField(choices=FACILITY_TYPE,default='parking')

    def __str__(self):
        return self.facility_type
class Review(BaseMixin):
    hotel = models.ForeignKey("Hotel",on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    star_rating = models.DecimalField(max_digits=2,decimal_places=1)
    
    def __str__(self):
        return f"{self.user.username} rated {self.hotel.name} {self.star_rating}"

class Hotel(BaseMixin):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    hotel_type = models.CharField(max_length=200,choices=HOTEL_TYPE,default='hotel')
    description = models.TextField(blank=True,null=True)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE,blank=True,null=True)
    manager = models.ForeignKey(User,on_delete=models.CASCADE,related_name='hotel_managers')
    contact = models.CharField(max_length=10)
    facilities = models.ManyToManyField(Facility,related_name='facility')
    
    def __str__(self):
        return f"Hotel {self.name} manager{self.address}"

class Room(BaseMixin):
    room_type = models.CharField(max_length=50,choices=ROOM_TYPE)
    room_number = models.CharField(max_length=10)
    description = models.TextField()
    person = models.IntegerField(default=1)
    hotel = models.ForeignKey("Hotel",on_delete=models.CASCADE,related_name='rooms')
    price = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    check_in = models.DateField(null=True,blank=True)
    check_out = models.DateField(null=True,blank=True)
    amenities = models.CharField(max_length=50,choices=AMENITIES)
    
    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}) {self.hotel.name}"

    