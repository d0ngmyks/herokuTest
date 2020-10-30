import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from ..app import app
from ...models import Specification

input1 = dbc.Row(
        [
            dbc.Col([
                dbc.InputGroup([
                    dbc.InputGroupAddon("Plate number", addon_type="prepend"),
                    dbc.Input(bs_size='lg', id='inputPlateNumber')
                ]),
            ], xs=8, className='mb-3'),
            dbc.Col([
                dbc.InputGroup([
                    dbc.InputGroupAddon("Fuel Type", addon_type="append"),
                    dbc.Select(
                        options=[
                            {"label": "Petrol", "value": 'P'},
                            {"label": "Diesel", "value": 'D'},
                            {"label": "Electric", "value": 'E'},
                        ],
                        bs_size='lg', id='selectFuelType'
                    )
                ]),
            ], xs=8, className='mb-3')]
    , justify='center'
)

layout = dbc.Card([
    dbc.Container(input1, fluid=True),
    html.Div('centered element', style={'width': '200px'}, className='mx-auto', id='testDiv'),
    dbc.InputGroup(
        [
            dbc.InputGroupAddon("Odometer", addon_type="prepend"),
            dbc.Input(className='mr-3', bs_size='lg'),
            dbc.InputGroupAddon("Odometer date as of", addon_type="append", className='ml-3'),
            dcc.DatePickerSingle(display_format='MMMM D, YYYY', clearable=True),
        ],
        className="mb-3",
    ),
    dbc.InputGroup(
        [
            dbc.InputGroupAddon("Other details", addon_type="prepend"),
            dbc.Textarea(bs_size='lg'),
        ],
        className="mb-3",
    ),
    dbc.Button('Save', color='success', block=True, id='btnSave_App1'),
], color='dark', inverse=True)


@app.callback(
    Output('testDiv', 'children'),
    [Input('btnSave_App1', 'n_clicks')],
    [State('inputPlateNumber', 'value'),
     State('selectFuelType', 'value')]
)
def display_value(n_clicks, plate, fuel, **kwargs):
    if n_clicks:  # can change to query if existing plate number
        save_vehicle(plate, fuel)
    return f'{plate}, {fuel} <br> zz'

def save_vehicle(plate, fuel):
    vehicle = Specification(plate_number=plate, fuel_type=fuel)
    vehicle.save()
