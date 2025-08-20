from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hotel.api_modules.views import (
    HotelViewSet, RoomViewSet, ReviewViewSet,
    FacilityViewSet, DestinationViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('v2/', include(router.urls))
]