import dash
import dash_bootstrap_components as dbc
from dash import html

from frontend.secundaria.izquerdo1.izquierdo1 import*

izquierdo1 = html.Div([
    html.H1("Especificaciones Técnicas del suelo"),
    html.P("Aquí se muestra la especificación correspondiente al tipo de suelo que mas se adecua a la clasidicación del usuario")
])
