from .app import dis
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc


dis.layout = html.Div(
    [
        dbc.Alert("This is an alert", id="base-alert", color="primary"),
        dbc.Alert(children="Danger", id="danger-alert", color="danger"),
        dbc.Button("External Link", id="update-button", color="warning", external_link=True, href='/vehicles/main-menu/'),
        dbc.Button("Link", id="update-button", color="warning", href='/apps/add-vehicle'),
    ]
)

@dis.expanded_callback(
    Output("danger-alert", 'children'),
    [Input('update-button', 'n_clicks'),]
    )
def session_demo_danger_callback(n_clicks, session_state=None, **kwargs):
    print('dash callback -- pipe-channel')
    # breakpoint()
    if session_state is None:
        raise NotImplementedError("Cannot handle a missing session state")
    csf = session_state.get('bootstrap_demo_state', None)
    if not csf:
        csf = dict(clicks=0)
        session_state['bootstrap_demo_state'] = csf
    else:
        csf['clicks'] = n_clicks
    return "Button has been clicked %s times since the page was rendered" %n_clicks
