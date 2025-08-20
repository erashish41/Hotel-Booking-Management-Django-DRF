from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from hotel.models import Hotel, Room, Facility, Destination, Review
from user_auth.models import User
from hotel.api_modules.serializers import (HotelSerializer, HotelMiniSerializer,
                                           RoomSerializer, ReviewSerializer,
                                           FacilitySerializer, DestinationSerializer,
                                           UserPublicSerializer
)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
        
    @action(methods=["get"], detail=True)
    def rooms(self, request,pk=None):
        hotel = self.get_object()
        serializer = RoomSerializer(
            hotel.rooms.all(), many=True
        )
        return Response(serializer.data) 

class HotelMiniViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelMiniSerializer
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
    @action(methods=["get"], detail=True)
    def hotel(self, request,pk=None):
        room = self.get_object()
        serializer = HotelSerializer(
            room.hotel.all(), many=True
        )
        return Response(serializer.data)
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer

