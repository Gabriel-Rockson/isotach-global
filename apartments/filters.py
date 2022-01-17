import django_filters

from apartments.models import Apartment


class ApartmentFilter(django_filters.FilterSet):

    class Meta:
        model = Apartment
        fields = {
            'bedrooms': ['gte'],
            'baths': ['gte'],
            'monthly_rent_payment': ['lt', 'gt'],
            'major_city': ['iexact'],
            'location': ['icontains'],
            'title': ['icontains'],
            'description': ['icontains'],
            'verified': ['exact'],
            'advance_years': ['gte']
        }