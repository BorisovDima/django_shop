from django.views.generic import DetailView
from django_filters.views import FilterView

from .filters import ProductFilter
from .mixins import KeyFromQueryStringMixin, JsonResponseMixin
from .models import Product



class MainPageView(JsonResponseMixin, FilterView):
    model = Product
    render_template = 'core/objects/products.html'
    template_name = 'core/mainpage.html'
    filterset_class = ProductFilter
    paginate_by = 8

    def get_json_data(self):
        return super().get_context_data(object_list=self.object_list)


class DetailProductView(JsonResponseMixin, KeyFromQueryStringMixin, DetailView):
    model = Product
    render_template = 'core/objects/detail-product.html'
    template_name = 'core/detail-product-main.html'

    def get_json_data(self):
        return {'product': self.object}

