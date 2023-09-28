import dash
import dash_bootstrap_components as dbc
from dash import html

derecho = dbc.Container([
    html.H1('Clasificación'),
    html.Hr(),
    html.Div(
        dbc.Button("Clasificar", color = "primary", className = "mr-2")
    )
        ,
])

