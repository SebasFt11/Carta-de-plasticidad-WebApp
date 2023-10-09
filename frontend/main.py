import dash
from dash import html
import dash_bootstrap_components as dbc

from .principal.navegador.navegador import navegador
from .principal.derecho.derecho import derecho
from .principal.izquierdo.izquierdo import izquierdo


layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Clasificación de Suelos',style = {'background-color': '#188EBE', 'color': 'white'}), md = 12),
    ]),
    dbc.Row([
        dbc.Col(navegador, md=12, style = {'background-color' : '#C9E2FF'}),
        dbc.Col(izquierdo, md=3, style = {'background-color' : '#E9F3FF'}),
        dbc.Col(derecho, md=9, style = {'background-color' : 'white'}),
    ])
])

from .secundaria.navegador1.navegador1 import navegador1
from .secundaria.derecho1.derecho1 import derecho1
from .secundaria.izquerdo1.izquierdo1 import izquierdo1


