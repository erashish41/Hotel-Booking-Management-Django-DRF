from django.contrib import admin
from hotel.models import Room, Hotel, Review, Facility, Destination

# Register your models here.
admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Facility)
admin.site.register(Destination)
