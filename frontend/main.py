import dash
from dash import html
import dash_bootstrap_components as dbc

from frontend.navegador.navegador import navegador
from frontend.derecho.derecho import derecho
from frontend.izquierdo.izquierdo import izquierdo

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