from rest_framework import serializers
from hotel.models import Hotel, Room, Review, Facility, Destination
from user_auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        



class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"
    

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
        
class HotelMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "name", "address", "hotel_type", "description"]

class ReviewSerializer(serializers.ModelSerializer):
    hotel = HotelMiniSerializer()
    user = UserSerializer()
    class Meta:
        model = Review
        fields = "__all__"
        
    
class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelMiniSerializer()
    class Meta:
        model = Room
        fields = "__all__"
        
        
class HotelSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()
    manager = UserSerializer()
    facilities = FacilitySerializer(many=True)
    class Meta:
        model = Hotel
        fields = "__all__"