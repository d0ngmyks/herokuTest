import dash_bootstrap_components as dbc
import dash_html_components as html
from django_plotly_dash import DjangoDash

buttons = html.Div(
    [
        dbc.Button("Regular", color="primary", className="mr-1"),
        dbc.Button("Active", color="primary", active=True, className="mr-1"),
        dbc.Button("Disabled", color="primary", disabled=True),
    ]
)

app = DjangoDash('VehiclesList')
app.css.append_css({'external_url':dbc.themes.BOOTSTRAP})
app.layout = buttons
