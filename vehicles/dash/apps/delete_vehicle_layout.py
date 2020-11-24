import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from ..app import app
from ...views import delete_vehicle
from ...models import Specification


# try:
#     vehicle_details = str(Specification.objects.get(pk=vehicle_id))
# except Specification.DoesNotExist:
#     vehicle_details = None


def modal_children(vehicle_id):
    return [
        dbc.ModalHeader("Delete vehicle"),
        dbc.ModalBody(str(Specification.objects.get(pk=vehicle_id))),
        dbc.ModalFooter(
            html.Div(
                className="ml-auto",
                children=[
                    dbc.Button(
                        id="cancel", color='secondary', children='Cancel',
                        href='/vehicles/main-menu/'
                    ),
                    dbc.Button(
                        id="delete", color='danger', children='Delete',
                        href=f'/confirm-delete/?q={vehicle_id}'
                    )
                ]
            )
        ),
    ]


@app.callback(
    Output('positioned-toast', 'is_open'),
    [
        Input('cancel', 'n_clicks'),
        Input('delete', 'n_clicks'),
    ],
    [State('delete', 'href')]
)
def confirm_deletion(n1, n2, href, **kwargs):
    print('# # # # # # # # # # # # # # # # # # # # # # # #')
    print("# # # # # # # # delete_vehicle_layout.py's callback # # # # # #")
    print('# # # # # # # # # # # # # # # # # # # # # # # #')
    if n1:
        return False
    elif n2:
        # returns the vehicle id from the href=f'/confirm-delete/?q={vehicle_id}'
        id = href.split(sep='?q=')[1]
        delete_vehicle(id)
        return True
