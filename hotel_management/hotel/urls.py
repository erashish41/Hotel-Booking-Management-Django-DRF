from django.urls import path
from hotel.views import (HotelListView, HotelCreateView, HotelDetailView, HotelDeleteView,
                        RoomListView, RoomCreateView, RoomDetailView, RoomDeleteView)

urlpatterns = [
    path('hotels/',HotelListView.as_view(),name='hotel_list'),
    path('hotels/create/',HotelCreateView.as_view(),name='hotel_create'),
    path('hotels/<uuid:pk>',HotelDetailView.as_view(),name='hotel_detail'),
    path('hotels/<uuid:pk>/delete',HotelDeleteView.as_view(),name='hotel_delete'),
    
    path('rooms/', RoomListView.as_view(),name='room_list'),
    path('rooms/create/',RoomCreateView.as_view(),name='room_create'),
    path('rooms/<uuid:pk>',RoomDetailView.as_view(),name='room_detail'),
    path('rooms/<uuid:pk>/delete',RoomDeleteView.as_view(),name='room_delete'),
]