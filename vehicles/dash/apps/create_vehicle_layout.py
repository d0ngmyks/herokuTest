import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dash import no_update
from django.utils import timezone

from ..app import app

from ...views import fuel_type_choices, save_vehicle

layout = dbc.Card(
    [
        dbc.CardHeader(dbc.Button('Cancel', outline=True, color='danger', href='/vehicles/main-menu/')),
        dbc.CardBody(
            [
                html.H5("Create vehicle", className="card-subtitle"),

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
                dcc.DatePickerSingle(
                    id='inputOdoDatePicker',
                    display_format='MMM D, YYYY',
                    clearable=True,
                    # with_portal=True,
                    date=timezone.now().strftime(format='%Y-%m-%d'),
                    className='mb-3'),

                # other_details
                html.Br(),
                dbc.Label('Other details', html_for='inputOtherDetails'),
                dbc.Textarea(id='inputOtherDetails', bs_size='lg')
            ],
            # style={'margin-top': '63px', 'margin-bottom': '63px'}
        ),
        dbc.CardFooter(
            dbc.Button('Save', color='success', block=True, id='btnSave_CreateVehicle',
                       href='/vehicles/main-menu/'),
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
        State('inputOdoDatePicker', 'date'),
        State('inputOtherDetails', 'value'),
        State('alert-fade', 'is_open')
    ]
)
def save_and_toggle_alert(n, plate_number, fuel_type, odometer, odo_date, other_details, is_open, **kwargs):
    if (plate_number and
            fuel_type and
            odometer and
            odo_date and
            other_details):
        # manual validation
        # (?) add dbc.formfeedback with the validations (?)
        save_vehicle(plate_number, fuel_type, odometer, odo_date, other_details)
    if n:
        return not is_open, f'New vehicle added: {plate_number}'
    return is_open, f'New vehicle added: {plate_number}'
