import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.dash import no_update

from .app import app

from ..views import Specification

app.layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                children=[

                    dbc.Row([
                        dbc.Col(html.H3('Vehicles')),
                        dbc.Col([
                            html.I(id='filter-vehicles', n_clicks=0, className='fa fa-filter fa-lg mr-2'),
                            html.I(className='fa fa-plus-square fa-lg mr-2'),
                        ], width='auto')
                    ], justify='between', align='center', no_gutters=True),

                    dbc.Row(dbc.Col(
                        dbc.InputGroup([
                            dbc.InputGroupAddon(dbc.Label(className='fa fa-search fa-lg pt-2 input-group-text', html_for='search_vehicle', style={'border-top-left-radius': '1rem', 'border-bottom-left-radius': '1rem'}), addon_type="prepend"),
                            dbc.Input(id='search_vehicle', type="search", placeholder="Search vehicles", style={'border-top-right-radius': '1rem', 'border-bottom-right-radius': '1rem'}),
                        ])
                    ), className='mb-2'),

                    dbc.Row(dbc.Col(
                        html.Div(id='dynamic-vehicles-list-container', children=[])
                    )),
                ],
                width=2),
            dbc.Col(
                id='selected-vehicle-container',
                children=['asd'],
                style={'border': '1px solid black'}, width=10
            ),
        ],
        no_gutters=True
    ),
], fluid=True)


@app.callback(
    Output('dynamic-vehicles-list-container', 'children'),
    [
        Input('filter-vehicles', 'n_clicks')
    ],
)
def load_vehicles_list(n, **kwargs):
    return dbc.ListGroup([
         dbc.ListGroupItem(
             id=f'{spec.id}',
             children=[spec.plate_number],
             n_clicks=0,
         )
         for spec in Specification.objects.all()
     ])


@app.callback(
    Output('selected-vehicle-container', 'children'),
    [
        Input(f'{spec.id}', 'n_clicks') for spec in Specification.objects.all()
    ]
)
def load_selected_vehicle(*args, **kwargs):
    triggered = kwargs['callback_context'].triggered
    if len(triggered) == 1:
        id = triggered[0]['prop_id'].replace('.n_clicks', '')
        return f'Vehicle with {id} is selected'
    else:
        return no_update
