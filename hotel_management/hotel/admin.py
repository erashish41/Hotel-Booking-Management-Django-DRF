from django.contrib import admin
from hotel.models import Room, Hotel, Review, Facility, Destination

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Facility)
admin.site.register(Destination)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_type', 'price', 'hotel',]
    search_fields = ['price']
    
admin.site.register(Room, RoomAdmin)