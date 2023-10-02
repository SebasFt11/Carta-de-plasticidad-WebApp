import dash
from dash import html
import dash_bootstrap_components as dbc

resultado = dbc.Card([
     dbc.CardHeader("Resultados"),
    dbc.CardBody([
        html.H5("Tu suelo es..."),
        html.P("Este suelo tiene las siguientes caracteristicas"),
        html.Div(id='resultado-clasificacion', className="p-4")
    ])
])