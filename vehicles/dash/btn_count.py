import dash_bootstrap_components as dbc
import dash_html_components as html
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output

button = html.Div(
    [
        dbc.Button("Click me", id="example-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)


app = DjangoDash('BtnCount')
app.css.append_css({'external_url':dbc.themes.BOOTSTRAP})
app.layout = button

@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."
