import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dash import no_update

from .app import app
from .apps import create_vehicle, app2

from ..views import get_all_vehicles

# 'plate_number', 'fuel_type', 'odometer', 'odo_date_as_of', 'other_details'
all_vehicles = get_all_vehicles()
dbc_all_vehicles = dbc.ListGroup(
    [dbc.ListGroupItem(vehicle.plate_number) for vehicle in all_vehicles],
    flush=True
)

main_menu = dbc.Card(
    [
        dbc.CardHeader(dbc.CardLink('Add Vehicle', href='/apps/add-vehicle')),
        dbc.CardBody(
            [
                # dbc.CardLink('Test django url', href='/vehicles/pipe-channel', external_link=True),
                # dbc.CardLink('Not external', href='/vehicles/pipe-channel'),
                # html.H4("Title", className="card-title"),
                html.H6("All Vehicles", className="card-subtitle"),
                # html.P(
                #     "Some quick example text to build on the card title and make "
                #     "up the bulk of the card's content.",
                #     className="card-text",
                # ),
                dbc_all_vehicles,
            ]
        ),

    ]
)

app.layout = html.Div(
    [
        dcc.Location(id='vehicle-url'),  # place here to avoid circular callbacks
        dbc.Alert(
            "Hello! I am an alert",
            id='alert-fade',
            dismissable=True,
            is_open=False,
        ),
        dbc.Container(
            dbc.Row(
                dbc.Col(dbc.Spinner(main_menu, id='main-spinner'),
                        sm={'size': 10, 'offset': 1},
                        md={'size': 8, 'offset': 2})
            ),
            fluid=True
        ),
        html.Span('--no-update--', id='current-path'),
    ],
)


@app.callback(
    [
        Output('main-spinner', 'children'),
        Output('current-path', 'children'),
    ],
    [
        Input('vehicle-url', 'pathname'),
    ]
)
def display_vehicles(pathname, **kwargs):
    print('dash callback ########')
    # breakpoint()
    if pathname == '/apps/add-vehicle':
        print(f'path-add-vehicle: {pathname}')
        return create_vehicle.layout, f'Current path is: {pathname}'
    elif pathname == '/vehicles/main-menu/':
        print(f'path-main-menu: {pathname}')
        return main_menu, f'Current path is: {pathname}'
    else:
        print('path-no-update: --no update--')
        return no_update, f'Current path is: {pathname}'
