from django.views.generic import DetailView
from django_filters.views import FilterView


from .filters import ProductFilter
from .mixins import KeyFromQueryStringMixin, JsonResponseMixin
from .models import Product

from celery import shared_task


class MainPageView(JsonResponseMixin, FilterView):
    model = Product
    render_template = 'core/objects/products.html'
    template_name = 'core/mainpage.html'
    filterset_class = ProductFilter
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.is_ajax():
            response = super().get_context_data(filter=self.filterset, object_list=self.object_list)
        return response


class DetailProductView(JsonResponseMixin, KeyFromQueryStringMixin, DetailView):
    model = Product
    render_template = 'core/objects/detail-product.html'
    template_name = 'core/detail-product-main.html'

    def get(self, req, *args, **kwarg):
        response = {'product': self.get_object()} if req.is_ajax() else super().get(req, *args, **kwarg)
        return response

