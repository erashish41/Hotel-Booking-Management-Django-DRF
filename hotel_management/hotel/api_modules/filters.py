import django_filters
from hotel.models import Hotel

class HotelFilter(django_filters.FilterSet):
    destination__city = django_filters.CharFilter(field_name="destination",lookup_expr="iexact")
    
    class Meta:
        model = Hotel
        fields = ["destination"]