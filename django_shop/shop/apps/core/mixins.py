from django.http import JsonResponse
from rest_framework.response import Response

class JsonMixin:
    pass


class KeyFromQueryStringMixin:
    lookup_query_key = None

    def dispatch(self, request, *args, **kwargs):
        value = request.GET.get(self.lookup_query_key)
        self.kwargs.update({self.lookup_query_key: value})
        return super().dispatch(request, *args, **self.kwargs)


class ListRestMixin:
    list_key = None

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({self.list_key: response.data})