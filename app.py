import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#importamos el frontend
from frontend.main import layout
from frontend.principal.navegador.navegador import *

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = layout
@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'active_tab')
)
def render_tab_content(active_tab):
    if active_tab == "tab-1":
        return tab_como_funciona
    elif active_tab == "tab-2":
        return tab_caracteristicas_suelo
    elif active_tab == "tab-3":
        return tab_clasificacion_suelos

# Callback para calcular y mostrar la clasificación del suelo
@app.callback(
    Output('resultado-clasificacion', 'children'),
    Input('button-clasifica', 'n_clicks'),
    State('dropdown-suelo', 'value')
)
def clasificar_suelo(n_clicks, valores_seleccionados):
    if n_clicks and valores_seleccionados:
       # Obtén los valores seleccionados
        permeabilidad = "Permeabilidad" in valores_seleccionados
        textura = "Textura del suelo" in valores_seleccionados
        materia = "Cantidad Materia órganica" in valores_seleccionados

        # Realiza la clasificación basada en los valores seleccionados
        if permeabilidad == "Alta" and textura == "Arcilloso" and materia == "Medio":
            resultado = "Clasificación del suelo: Horizonte B"
        else:
            resultado = "Clasificación del suelo: No se pudo determinar la clasificación"
        return resultado  # Corrected: Return the classification result
    else:
        return ""
    
if __name__ =='__main__':
    app.run_server(debug=True)
