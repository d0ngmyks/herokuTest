from django.views.generic import ListView
from .models import Specification

class VehiclesListView(ListView):
    template_name = 'vehicles/list.html'
    model = Specification

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breakpoint()
        import dash_bootstrap_components as dbc

        button = dbc.Button("Block button", color="primary", block=True)
        context['button'] = button
        return context
