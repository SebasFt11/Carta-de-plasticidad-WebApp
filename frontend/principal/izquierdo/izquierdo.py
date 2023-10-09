import dash
import dash_bootstrap_components as dbc
from  dash import html

izquierdo = dbc.Container([
    html.Div([
        html.Img(src= 'Suelo.png', alt = 'portada', style={'max-width': '100%'}),
    ])
])