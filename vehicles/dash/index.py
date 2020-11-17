import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dash import no_update

from .app import app
from .apps import create_vehicle, app2

from ..views import get_all_vehicles

app.layout = html.Div(
    [
        dcc.Location(id='vehicle-url'),  # place here to avoid circular callbacks
        dbc.Alert(id='alert-fade', dismissable=True, duration=3000, is_open=False, fade=True),
        dbc.Container(fluid=True, children=[
            dbc.Row(
                dbc.Col(
                    sm={'size': 10, 'offset': 1},
                    md={'size': 8, 'offset': 2},
                    children=[dbc.Spinner(id='main-spinner')]
                )
            ),
            # test
            html.Div(id='test-div')
        ])
    ],
)


@app.callback(
    [
        Output('test-div', 'children'),
        Output('main-spinner', 'children'),
    ],
    [
        Input('vehicle-url', 'pathname')
    ],
)
def display_vehicle_card(pathname, **kwargs):
    print('# # # # # # # # # # # # # # # # # # # # # # # #')
    print("# # # # # # # # index.py's callback # # # # # #")
    print('# # # # # # # # # # # # # # # # # # # # # # # #')

    if (pathname == '/django_plotly_dash/app/VehiclesDashApp/' or
            pathname == '/vehicles/main-menu/'):
        # (initial) load from Django's url called from view or back button
        result = []
        for vehicle in get_all_vehicles():
            result.append(
                dbc.ListGroupItem(
                    action=True,
                    children=[vehicle.plate_number,
                    dbc.ButtonGroup([dbc.Button('Edit'), dbc.Button('Delete')], className='float-right')],
                )
            )

        main_menu = dbc.Card(
            [
                dbc.CardHeader(dbc.CardLink('Add vehicle', href='/apps/add-vehicle/')),
                dbc.CardBody(
                    [
                        html.H5("All vehicles", className="card-subtitle"),  # can add filtering
                        dbc.ListGroup(
                            flush=True,
                            children=result,
                            # children=[dbc.ListGroupItem([dbc.InputGroup([vehicle.plate_number, dbc.InputGroupAddon(dbc.Button('Hello'), addon_type='append')])], action=True) for vehicle in get_all_vehicles()],
                            # children=[dbc.ListGroupItem([vehicle.plate_number, dbc.Button('Hello')], action=True) for vehicle in get_all_vehicles()],
                        )
                    ]
                ),
            ]
        )
        return f'Current path name is {pathname}', main_menu
    elif pathname == '/apps/add-vehicle/':
        return f'Current path name is {pathname}', create_vehicle.layout
