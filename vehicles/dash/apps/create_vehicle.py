import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from ..app import app

from ...views import fuel_type_choices, save_vehicle

from django.utils import timezone


layout = dbc.Card(
    [
        dbc.CardHeader(
            # dbc.Navbar([
                [
                    dbc.Button('Cancel', outline=True, color='danger', href='/vehicles/main-menu/'),
                ]
            # ], fixed='top'),
            # className='fixed-top bg-light',
        ),
        dbc.CardBody(
            [
                # plate_number
                dbc.Label('Plate number', html_for='inputPlateNumber'),
                dbc.Input(id='inputPlateNumber', bs_size='lg', maxLength=8, className='mb-3'),

                # fuel type
                dbc.Label('Fuel type', html_for='selectFuelType'),
                html.Br(),
                dbc.Select(options=fuel_type_choices(), bs_size='lg', id='selectFuelType', className='mb-3'),

                # odometer
                html.Br(),
                dbc.Label('Odometer', html_for='inputOdometer'),
                dbc.Input(id='inputOdometer', bs_size='lg', type='number', step=0.1, className='mb-3'),

                # odo_date_as_of
                dbc.Label('Odometer date as of'),
                html.Br(),
                dcc.DatePickerSingle(display_format='MMM D, YYYY', date=timezone.now(), clearable=True,
                                     id='inputOdoDatePicker', with_portal=True, className='mb-3'),

                # other_details
                html.Br(),
                dbc.Label('Other details', html_for='inputOtherDetails'),
                dbc.Textarea(id='inputOtherDetails', bs_size='lg')
            ],
            # style={'margin-top': '63px', 'margin-bottom': '63px'}
        ),
        dbc.CardFooter(
            dbc.Button('Save', color='success', block=True, id='btnSave_CreateVehicle', href='/vehicles/main-menu/'),
            # className='fixed-bottom bg-light',
        ),
    ]
)


@app.callback(
    [
        Output('alert-fade', 'is_open'),
        Output('alert-fade', 'children'),
    ],
    [Input('btnSave_CreateVehicle', 'n_clicks')],
    [
        State('inputPlateNumber', 'value'),
        State('selectFuelType', 'value'),
        State('inputOdometer', 'value'),
        State('inputOdoDatePicker', 'value'),  # not value?
        State('inputOtherDetails', 'value'),
        State('alert-fade', 'is_open')
    ]
)
def save_and_toggle_alert(n, plate_number, fuel_type, odometer, odo_date, other_details, is_open, **kwargs):
    if plate_number and fuel_type and odometer and other_details:
    # if plate_number and fuel_type and odometer and odo_date and other_details:
        print(plate_number, fuel_type, odometer, odo_date, other_details)
        # save_vehicle(plate_number, fuel_type, odometer, odo_date, other_details)
        from ...models import Specification
        vehicle = Specification(plate_number=plate_number, fuel_type=fuel_type, odometer=odometer,
                                odo_date_as_of=odo_date, other_details=other_details)
        vehicle.save()
    if n:
        return not is_open, f'New vehicle added: {plate_number}'
    return is_open, f'New vehicle added: {plate_number}'

# @app.callback(
#     [
#         Output('alert-fade', 'is_open')
#         # Output('main-spinner', 'children'),
#     ],
#     [
#         Input('btnSave_CreateVehicle', 'n_clicks'),
#     ],
#     [
#         # State('inputPlateNumber', 'value'),
#         # State('selectFuelType', 'value'),
#         # State('inputOdometer', 'value'),
#         # State('inputOdoDatePicker', 'value'),
#         # State('inputOtherDetails', 'value'),
#         State('alert-fade', 'is_open')
#     ]
# )
# def toggle_alert(n, is_open, **kwargs):  # def toggle_alert(n, plate_number, fuel_type, odometer, odo_date, other_details, is_open, **kwargs):
#     breakpoint()
#     print('dash -- create_vehicle.py')
#     # save_vehicle(plate_number, fuel_type, odometer, odo_date, other_details)
#     if n:
#         return not is_open
#     return is_open

# def display_value(n_clicks, plate, fuel, odometer, odo_date, other_details, **kwargs):
#     print('dash -- create_vehicle.py')
#     if n_clicks:  # can change to query if existing plate number
#         save_vehicle(plate, fuel, odometer, odo_date, other_details)
#     return f'{plate}, {fuel} <br> zz'
