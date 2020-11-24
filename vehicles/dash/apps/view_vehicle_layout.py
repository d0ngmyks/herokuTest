import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from django.utils import timezone

from ..app import app

from ...views import fuel_type_choices, save_vehicle
from ...models import Specification


def card(vehicle_id):
    vehicle_details = Specification.objects.get(pk=vehicle_id)
    return dbc.Card(
        [
            dbc.CardHeader(
                dbc.Button(
                    'Back',
                    outline=True, color='secondary',
                    # href='/vehicles/main-menu/',
                    href='javascript:history.back()',
                    # https://stackoverflow.com/questions/8814472/how-to-make-an-html-back-link
                )),
            dbc.CardBody(
                [
                    html.H5(vehicle_id, className="card-subtitle"),

                    # plate_number
                    dbc.Label('Plate number', html_for='inputPlateNumber'),
                    dbc.Input(
                        id='inputPlateNumber',
                        value=vehicle_details.plate_number,
                        disabled=True,
                        bs_size='lg', maxLength=8, className='mb-3'
                    ),

                    # fuel type
                    dbc.Label('Fuel type', html_for='selectFuelType'),
                    html.Br(),
                    dbc.Select(
                        id='selectFuelType',
                        value='P',
                        disabled=True,
                        options=fuel_type_choices(),
                        bs_size='lg', className='mb-3'
                    ),

                    # odometer
                    html.Br(),
                    dbc.Label('Odometer', html_for='inputOdometer'),
                    dbc.Input(
                        id='inputOdometer',
                        value=vehicle_details.odometer,
                        bs_size='lg', type='number', step=0.1, className='mb-3'
                    ),

                    # odo_date_as_of
                    dbc.Label('Odometer date as of'),
                    html.Br(),
                    dcc.DatePickerSingle(
                        id='inputOdoDatePicker',
                        display_format='MMM D, YYYY',
                        clearable=True,
                        # with_portal=True,
                        date=timezone.now().strftime(format='%Y-%m-%d'),
                        className='mb-3',
                    ),

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
