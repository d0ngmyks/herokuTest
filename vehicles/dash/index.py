import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dash import no_update

from .app import app
from .apps import create_vehicle_layout, delete_vehicle_layout

from ..views import get_all_vehicles

app.layout = html.Div(
    [
        dcc.Location(id='vehicle-url'),  # place here to avoid circular callbacks
        dbc.Alert(id='alert-fade', dismissable=True, duration=3000, is_open=False, fade=True),
        html.Div(
            style={'position': 'absolute', 'left': '50%'},
            children=[
                dbc.Toast(
                    "A vehicle has been deleted.",
                    id="positioned-toast",
                    header="Vehicles", header_style={'color': '#CCCCCC'},
                    is_open=False,
                    dismissable=True,
                    icon="success",
                    duration=2000,
                    # style={"position": "fixed", "top": 66, "right": 10, "width": 350},
                    style={'z-index': '1050', 'position': 'relative', 'left': '-50%', 'width': 200},
                ),
            ]
        ),
        dbc.Modal(id='main-modal', backdrop='static', centered=True),
        dbc.Container(fluid=True, children=[
            dbc.Row(
                dbc.Col(
                    sm={'size': 10, 'offset': 1},
                    md={'size': 8, 'offset': 2},
                    children=[
                        dbc.Spinner(id='main-spinner')
                    ]
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
            pathname == '/vehicles/main-menu/' or
            pathname == '/confirm-delete/'):
        # (initial) load from Django's url called from view or back button
        result = []
        # for idx, vehicle in enumerate(get_all_vehicles()):
        for vehicle in get_all_vehicles():
            result.append(
                dbc.ListGroupItem(
                    className='hoverable-listgroup-item',
                    action=True,
                    href='#',
                    children=[
                        vehicle.plate_number,
                        html.Div(
                            className='show-on-hover float-right',
                            children=[
                                dbc.Button(
                                    id='btnEditVehicle',
                                    className='fa fa-pencil fa-lg', color='primary',
                                    outline=True, style={'border': 'none'}
                                ),
                                dbc.Button(
                                    id='btnDeleteVehicle',
                                    className='fa fa-trash-o fa-lg', color='danger',
                                    outline=True, style={'border': 'none'},
                                    href=f'/apps/delete-vehicle/?q={vehicle.id}'
                                ),
                            ],
                        ),
                    ]
                )
            )

        main_menu = dbc.Card(
            [
                dbc.Tooltip('Edit', target='btnEditVehicle') if result else '',
                dbc.Tooltip('Delete', target='btnDeleteVehicle') if result else '',
                dbc.CardHeader(dbc.CardLink('Add vehicle', href='/apps/add-vehicle/')),
                dbc.CardBody(
                    [
                        html.H5("All vehicles", className="card-subtitle"),  # can add filtering
                        dbc.ListGroup(
                            flush=True,
                            children=result if result else dbc.ListGroupItemText('No records found.')
                        )
                    ]
                ),
            ]
        )
        return f'Current path name is {pathname}', main_menu
    elif pathname == '/apps/add-vehicle/':
        return f'Current path name is {pathname}', create_vehicle_layout.layout
    # elif pathname == '/apps/delete-vehicle/':
    #     print('* * * main-menu delete button * * *')
    #     search = str(search).replace('?q=', '')
    #     return f'Current path name is {pathname}', delete_vehicle_layout.confirm_delete_modal(search)
    else:
        return f'Current path name is {pathname}', no_update


@app.callback(
    [
        Output('main-modal', 'is_open'),
        Output('main-modal', 'children'),
    ],
    [Input('vehicle-url', 'pathname')],
    [State('vehicle-url', 'search')]
)
def toggle_main_modal(pathname, search, **kwargs):
    if pathname == '/apps/delete-vehicle/':
        search = str(search).replace('?q=', '')
        # return delete_vehicle_layout.modal_children(search)
        # if n1 or n2:
        #     return not is_open
        return True, delete_vehicle_layout.modal_children(search)
    else:
        return False, no_update
