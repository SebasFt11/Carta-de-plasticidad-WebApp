import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

textura =dbc.Card([
     dbc.CardBody(
            [
                html.H5("Textura del suelo", className="card-title")]),
     dcc.Dropdown(
            ['Franco', 'Turboso', 'Pedregoso','Arenoso','Arcilloso'])
])