import django_filters

from apartments.models import Apartment

PRICES = (
    (100, 'Ghc 100.00'),
    (300, 'Ghc 300.00'),
    (500, 'Ghc 500.00'),
    (700, 'Ghc 700.00'),
    (1000, 'Ghc 1000.00'),
    (1200, 'Ghc 1200.00'),
    (1400, 'Ghc 1400.00'),
    (1600, 'Ghc 1600.00'),
    (1800, 'Ghc 1800.00'),
    (2000, 'Ghc 2000.00'),
    (2500, 'Ghc 2500.00'),
    (3000, 'Ghc 3000.00'),
    (3500, 'Ghc 3500.00'),
    (4000, 'Ghc 4000.00'),
    (4500, 'Ghc 4500.00'),
)

BOOL_OPTIONS = (
    (True, "Yes"),
    (False, "No"),
)


class ApartmentFilter(django_filters.FilterSet):

    major_city = django_filters.ChoiceFilter(
        choices=Apartment.MajorCity.choices)
    bedrooms = django_filters.ChoiceFilter(choices=Apartment.Number.choices,
                                           lookup_expr="gte")
    baths = django_filters.ChoiceFilter(choices=Apartment.Number.choices,
                                        lookup_expr="gte")
    advance_years = django_filters.ChoiceFilter(
        choices=Apartment.Number.choices, lookup_expr="gte")
    monthly_rent_payment__gt = django_filters.ChoiceFilter(
        choices=PRICES, field_name='monthly_rent_payment', lookup_expr='gt')
    monthly_rent_payment__lt = django_filters.ChoiceFilter(
        choices=PRICES, field_name='monthly_rent_payment', lookup_expr='lt')
    verified = django_filters.ChoiceFilter(choices=BOOL_OPTIONS,
                                           field_name='verified')
    location = django_filters.CharFilter(field_name="location",
                                         lookup_expr="icontains")

    def __init__(self, *args, **kwargs):
        super(ApartmentFilter, self).__init__(*args, **kwargs)
        self.filters['major_city'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['bedrooms'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['baths'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['advance_years'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['monthly_rent_payment__gt'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['monthly_rent_payment__lt'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['verified'].field.widget.attrs.update(
            {'class': 'filter-item-select'})
        self.filters['location'].field.widget.attrs.update({
            'class':
            'filter-item-input',
            'placeholder':
            'Enter City or Town'
        })

    class Meta:
        model = Apartment
        fields = [
            "major_city", "bedrooms", "baths", "advance_years",
            "monthly_rent_payment__gt", "monthly_rent_payment__lt", "verified",
            "location"
        ]
