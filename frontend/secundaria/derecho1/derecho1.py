import dash
import dash_bootstrap_components as dbc
from dash import html

from frontend.secundaria.derecho1.derecho1 import*

derecho1 = html.Div([
    html.H1("Descripción del suelo"),
    html.P("Aquí se muestra la descripción del suelo según la clasificación que el usuario escogiese")
])

