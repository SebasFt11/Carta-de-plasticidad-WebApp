import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

permeabilidad = dbc.Card([
     dbc.CardBody(
            [
                html.H5("Permeabilidad", className="card-title")]),
     dcc.Dropdown(
            ['Baja', 'Media', 'Alta']
        ),
])