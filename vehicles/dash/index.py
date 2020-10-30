import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from .app import app
from .apps import create_vehicle, app2


modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("This modal is vertically centered"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-centered", className="ml-auto"
                    )
                ),
            ],
            id="modal-centered",
            centered=True,
        ),
    ]
)

index = dbc.Spinner(dbc.Card([
    dcc.Location(id='url', refresh=False),
    dbc.CardHeader(
        [html.Img(src='assets/control.jpg', height='75px', width='75px'),
        dbc.Button('Add Vehicle', color='primary', id='btnOpenModal'),
         modal,
         dbc.Row(dbc.Col(dcc.Link(
             dbc.Button('Add Vehicle', color='primary'),
             href='/apps/add-vehicle'
         ),
             width=4),
             id='linkBtnAddVehicle',
             justify='end',
             style={'height': '150px'},
             align='center',
         ),
         html.H3('Lorem Ipsum', id='h3AddVehicle', hidden=True)]
    ),
    dbc.CardBody([
        html.H5("Plate number (?)", className="card-title"),
        html.P(
            "This is some card content that we'll reuse",
            className="card-text",
        ),
        dbc.Button('Edit (?)', color='success'),
        dbc.Button('Another Button (?)', color='warning')
    ]),

    html.Div(dbc.Button('Cancel', color='danger', href='/apps/cancel'),
             id='btnCancel', hidden=True),

    html.Div(id='page-content'),
]))

# app.layout = dbc.Row(
#     dbc.Col([
#         index
#     ], xs=8)
# , justify='center')

app.layout = index

@app.callback(
    [Output('page-content', 'children'),
     Output('linkBtnAddVehicle', 'hidden'),
     Output('h3AddVehicle', 'hidden'),
     Output('btnCancel', 'hidden'),],
    [Input('url', 'pathname')])
def display_page(pathname, **kwargs):
    # breakpoint()
    if pathname == '/apps/add-vehicle':
        return create_vehicle.layout, True, False, False
    elif pathname == '/apps/cancel':
        return app2.layout, False, True, True
    else:
        return None, False, True, True


@app.callback(
    Output("modal-centered", "is_open"),
    [Input("btnOpenModal", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open, **kwargs):
    if n1 or n2:
        return not is_open
    return is_open
