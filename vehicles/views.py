from django.views.generic import ListView
from .models import Specification
from django.shortcuts import render

# class VehiclesListView(ListView):
#     template_name = 'vehicles/list.html'
#     model = Specification
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print('called by dcc.location?')
#         print('called by dcc.location?')
#         print('called by dcc.location?')
#         print('called by dcc.location?')
#         context['DjangoGCD'] = 'This is from Django''s view'
#         # import dash_bootstrap_components as dbc
#
#         # button = dbc.Button("Block button", color="primary", block=True)
#         # context['button'] = button
#         # context['plotly_sample'] = 'SimpleExample'
#         print(context)
#         return context
def console_print():
    return print('# # # # # # # # # # # # # # # # # # # # # # # #'),\
           print("# # # # # # # # Django's views # # # # # # # #"),\
           print('# # # # # # # # # # # # # # # # # # # # # # # #')

def vehicles_app(request):
    console_print()
    print('render vehicles/list.html')
    # breakpoint()
    return render(request, 'vehicles/list.html')

def pipe_channel(request):
    print('django view -- dash session state')
    # breakpoint()
    return render(request, 'vehicles/test-pipe-channel.html')

def get_all_vehicles():
    from .models import Specification
    queryset = Specification.objects.all()
    return queryset

def selected_vehicle(id):
    vehicle = Specification.objects.get(pk=id)

def fuel_type_choices():
    fuel_type_choices = []
    for value, label in Specification.fuel_type.field.choices:
        fuel_type_choices.append({'value': value, 'label': label})
    return fuel_type_choices

def save_vehicle(plate_number, fuel_type, odometer, odo_date_as_of, other_details):
    vehicle = Specification(plate_number=plate_number, fuel_type=fuel_type, odometer=odometer, odo_date_as_of=odo_date_as_of, other_details=other_details)
    vehicle.save()

def delete_vehicle(id):
    vehicle = Specification.objects.get(pk=id)
    vehicle.delete()
