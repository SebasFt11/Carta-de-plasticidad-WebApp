import dash
import dash_bootstrap_components as dbc
from dash import html

from frontend.principal.derecho.textura import *
from frontend.principal.derecho.permeabilidad import *
from frontend.principal.derecho.materia import *
from frontend.principal.derecho.clasifica import *
from frontend.principal.derecho.resultado import *

derecho = dbc.Container([
    html.H1('Clasificación'),
    html.Hr(),
    html.Div(
        dbc.Button("Clasificar", color = "primary", className = "mr-2")
    )
        ,
])

import dash
import dash_bootstrap_components as dbc

from frontend.principal.derecho.textura import *
from frontend.principal.derecho.permeabilidad import *
from frontend.principal.derecho.materia import *
from frontend.principal.derecho.clasifica import *
from frontend.principal.derecho.resultado import *

derecho = dbc.Container([
    dbc.Row([
        dbc.Col(textura, md=4,style = {'background-color' : '#F4F9FF', 'color' : 'black', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
        dbc.Col(permeabilidad, md=4,style = {'background-color' : '#F4F9FF', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
        dbc.Col(materia, md=4,style = {'background-color' : '#F4F9FF', 'border-top' : '5px solid #055E97'}),
        dbc.Col(clasifica,),
        dbc.Col(resultado, md=12)
    ])
])