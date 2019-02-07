from django.template.loader import render_to_string
from django.http.response import JsonResponse

class JsonResponseMixin:
    render_key = 'html'
    render_template = None

    def get_extra_json(self):
        return {}

    def dispatch(self, request, *args, **kwargs):
        data = super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            if self.render_template:
                data = render_to_string(self.render_template, data, request)
            json_context = {self.render_key: data}
            json_context.update(self.get_extra_json())
            data = JsonResponse(json_context)
        return data



class KeyFromQueryStringMixin:
    lookup_query_key = 'pk'

    def dispatch(self, request, *args, **kwargs):
        value = request.GET.get(self.lookup_query_key)
        if value:
            self.kwargs.update({self.lookup_query_key: value})
        return super().dispatch(request, *args, **self.kwargs)






