from hotel.models import Hotel, Room, Review, Destination, Facility
from django import forms

class HotelCreateForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"
        
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        