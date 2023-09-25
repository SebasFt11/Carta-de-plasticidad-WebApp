import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container((
    html.H1('Clasificación de suelos'),
    html.Hr(),
    html.H2('Sebastian David Lopez'),
    dbc.Row([
         dbc.Col("visualización", md=3, style = {'background-color' : 'black', 'color' : 'white'}),
         dbc.Col("texto", md=6, style = {'background-color' : 'gray'}),
         dbc.Col("usuario", md=3, style = {'background-color' : 'yellow'}),
    ])
))