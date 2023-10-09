import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

materia = dbc.Card([
     dbc.CardBody(
            [
                html.H5("Cantidad Materia órganica", className="card-title")]),
     dcc.Dropdown(
            ['Bajo', 'Medio', 'Alto']
        ),
])