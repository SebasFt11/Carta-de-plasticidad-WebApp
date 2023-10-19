import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#importamos el frontend
from frontend.main import layout
from frontend.navegador.navegador import *

#importamos el backend
from backend.carta import cartaPlasticidad

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = layout

# Callback para mostrar texto basado en la opción seleccionada
@app.callback(
    dash.dependencies.Output('texto-seleccionado', 'children'),
    dash.dependencies.Input('dropdown-opciones', 'value')
)
def mostrar_texto(opcion_seleccionada):
    texto = {
        'MH': "Suelo MH (Materiales de Alta Plasticidad): Este tipo de suelo tiene un alto índice de plasticidad y un alto límite líquido. "
              "Son suelos muy plásticos que pueden cambiar de forma significativamente bajo carga. Tienden a retener una cantidad considerable "
              "de agua, lo que los hace propensos a la expansión y contracción. Los suelos MH son comunes en áreas con alto contenido de arcilla. "
              "En la construcción, se deben tomar precauciones para evitar problemas de cimentación y estabilidad.",
        'CL': "Suelo CL (Materiales con Límite de Plasticidad Bajo): Este tipo de suelo tiene un bajo índice de plasticidad y un bajo límite líquido. "
              "Son suelos no plásticos y no retienen mucha agua. Los suelos CL son típicos en regiones con suelos arenosos o gravas. Son adecuados "
              "para la construcción de estructuras ligeras y no presentan problemas significativos de expansión o contracción.",
        'CH': "Suelo CH (Materiales de Alta Plasticidad): Los suelos CH tienen un alto índice de plasticidad y un alto límite líquido, lo que los "
              "hace muy plásticos y capaces de retener una gran cantidad de agua. Se encuentran en áreas con arcillas expansivas y son propensos a cambios "
              "volumétricos significativos con cambios de humedad. En la construcción, es importante tomar medidas para controlar la expansión y la contracción.",
        'ML': "Suelo ML (Materiales con Límite de Plasticidad Bajo): Estos suelos tienen un bajo índice de plasticidad y un bajo límite líquido. No son muy "
              "plásticos y retienen una cantidad limitada de agua. Los suelos ML son comunes en suelos que son una mezcla de arcilla y arena. Son adecuados "
              "para construcción de caminos y estructuras ligeras.",
        'NO EXISTE': "El punto no se encuentra en la carta de plasticidad."
    }
    return texto.get(opcion_seleccionada, "No se ha seleccionado una opción válida.")



#Definimos los tabs
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

#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])
    
if __name__ =='__main__':
    app.run_server(debug=True)
