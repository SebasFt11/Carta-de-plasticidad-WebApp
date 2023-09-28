import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container((
    html.H1('Clasificación de suelos', style = {'color': 'white'}),
    html.Hr(style = {"border-color" : "white", "border-width" : "5px"}),
    html.H2('Sebastian David Lopez', style = {'color': 'white'}),
    html.Img(src='/assets/imagenes/mi_imagen.jpg', alt='Mi Imagen', style={'max-width': '100%'}),

    dbc.Row([
         dbc.Col("¿Cómo funciona?", md=3, style = {'height' : '40px','background-color' : '#B4D6E4', 'color' : 'black', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
         dbc.Col("Características del suelo", md=6, style = {'background-color' : '#B4D6E4', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
         dbc.Col("¿Qué suelo tengo?", md=3, style = {'background-color' : '#B4D6E4', 'border-top' : '5px solid #055E97'}),
    ])
))