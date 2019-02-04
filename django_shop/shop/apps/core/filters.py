from django_filters import FilterSet, OrderingFilter
from .models import Product

CHOICES =[
        ["name", "по алфавиту"],
        ["price", "дешевые сверху"],
        ["-price", "дорогие сверху"]
]

class ProductFilter(FilterSet):
    ordering = OrderingFilter(choices=CHOICES, required=True, empty_label=None)

    class Meta:
        model = Product
        fields = {'price':  ['lt', 'gt'],
                  'category': ['exact'],
                  'name': ['icontains'],
                  'brand': ['exact'],
                  }