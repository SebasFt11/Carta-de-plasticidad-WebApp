from dash import html  # Importa los componentes necesarios de la libreria de Dash
import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components

from frontend.navegador.navegador import navegador  # Importar la variable "navegador" de la carpeta del frontend
from frontend.derecho.derecho import derecho  # Importar la variable "derecho" de la carpeta del frontend
from frontend.izquierdo.izquierdo import izquierdo    # Importar la variable "izquierdo" de la carpeta del frontend


# Crear el diseño de la página web
layout = dbc.Container([  # Se crea un contenedor de Dash que señala los elementos que contendrán la página.
    dbc.Row([  # Crear una fila para el encabezado
        dbc.Col(html.H1('Clasificación de Suelos',style = {'background-color': '#188EBE', 'color': 'white'}), md = 12),  # Crear una columna que contiene un título de nivel 1 y su estilo
    ]),
    dbc.Row([  # Crear una fila para los contenidos principales
        dbc.Col(navegador, md=12, style = {'background-color' : '#C9E2FF'}),  # Crear una columna que contiene el componente "navegador", que se importa de otra carpeta donde ya esta definida y el estilo de esta
        dbc.Col(izquierdo, md=3, style = {'background-color' : '#E9F3FF'}),  # Crear una columna que contiene el componente "izquierdo", que se importa de otra carpeta donde ya esta definida y el estilo de esta
        dbc.Col(derecho, md=9, style = {'background-color' : 'white'}),  # Crear una columna que contiene el componente "derecho", que se importa de otra carpeta donde ya esta definida y el estilo de esta
    ])
])