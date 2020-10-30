from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

app = DjangoDash('VehiclesDashApp', expanded_callbacks=True,  add_bootstrap_links=True)
# app.css.append_css({'external_url':dbc.themes.BOOTSTRAP})

# app.css.append_css({'relative_package_path': ''})  # elephantttttt for icons!
