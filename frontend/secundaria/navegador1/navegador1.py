import dash
import dash_bootstrap_components as dbc
from dash import html

from frontend.secundaria.navegador1.navegador1 import*

navegador1 = html.Div([
    html.H1("Tipos de suelo relacionados"),
    dbc.Button("Volver a iniciio", id = "back-to-main-page-button")
])