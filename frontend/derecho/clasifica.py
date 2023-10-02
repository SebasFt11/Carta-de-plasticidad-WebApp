import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

from .derecho import permeabilidad
from .derecho import materia
from .derecho import textura



clasifica = dbc.Card([
    dbc.CardBody([
        dcc.Dropdown(
        id='dropdown-suelo',
        options=[
            {'label': permeabilidad, 'value': permeabilidad},
            {'label': materia, 'value': materia},
            {'label': textura, 'value': textura}
        ],
        multi=True
    ),
    dbc.Button("Clasifica", id='button-clasifica', color="primary"),
    ])
])