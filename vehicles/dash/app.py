from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

app = DjangoDash(
    'VehiclesDashApp',
    expanded_callbacks=True,
    add_bootstrap_links=True,
    suppress_callback_exceptions=True,
)

# app.css.append_css({'external_url':dbc.themes.BOOTSTRAP})
app.css.append_css({'external_url':'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'})
app.css.append_css({'external_url':'assets/hover-me.css'})

# app.css.append_css({'relative_package_path': ''})  # (?) elephantttttt for icons!

dis = DjangoDash("DjangoSessionState", expanded_callbacks=True, add_bootstrap_links=True)
