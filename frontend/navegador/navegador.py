import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container([
    dbc.Tabs(
        [
            dbc.Tab(label="¿Cómo funciona?", tab_id="tab-1", style = {'height' : '40px','background-color' : '#B4D6E4', 'color' : 'black', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
            dbc.Tab(label="Caracteristicas del suelo", tab_id="tab-2",style = {'background-color' : '#B4D6E4', 'border-top' : '5px solid #055E97', 'border-right' : '1px solid white'}),
            dbc.Tab(label="¿Qué suelo tengo?", tab_id="tab-3",style = {'background-color' : '#B4D6E4', 'border-top' : '5px solid #055E97'})
        ],
        id="tabs",
        active_tab="tab-1",
    ),

    html.Div(id="tab-content", className="p-4"),
])
        