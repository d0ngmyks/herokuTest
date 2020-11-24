from django_plotly_dash import DjangoDash


app = DjangoDash(
    'VehiclesDashApp2',
    expanded_callbacks=True,
    add_bootstrap_links=True,
    suppress_callback_exceptions=True,
    # serve_locally=True,
)

# app.css.append_css({'external_url':dbc.themes.BOOTSTRAP})
app.css.append_css({'external_url':'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'})
