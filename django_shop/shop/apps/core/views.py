from .models import Product
from django_filters.views import FilterView
from .filters import ProductFilter
from django.views.generic.list import MultipleObjectMixin

class MainPage(FilterView):
    model = Product
    template_name = 'core/mainpage.html'
    filterset_class = ProductFilter
    paginate_by = 5

    def get_context_data(self, **kwargs):
        con = super().get_context_data( **kwargs)
        print(con)
        return con


