import dash
import dash_bootstrap_components as dbc
from  dash import html, dcc

izquierdo = dbc.Container([
    dcc.Dropdown(
        id='dropdown-opciones',
        options=[
            {'label': 'MH', 'value': 'MH'},
            {'label': 'CL', 'value': 'CL'},
            {'label': 'CH', 'value': 'CH'},
            {'label': 'ML', 'value': 'ML'},
            {'label': 'NO EXISTE', 'value': 'NO EXISTE'}
        ],
        value='MH'  # Opción predeterminada
    ),
    html.Div(id='texto-seleccionado', className="p-4"),
])