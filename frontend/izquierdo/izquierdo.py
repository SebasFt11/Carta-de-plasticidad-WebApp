import dash
import dash_bootstrap_components as dbc
from  dash import html,dcc

izquierdo = dbc.Container([
    html.H1('Zona de visualización'),
    html.Hr(),
    html.Div([
        html.Label('Area del circulo'),
        dcc.Input(id = 'entradaCirculo', value = 5, type = 'number'),
        html.Label(id = 'salidaCirculo')

    ])
])