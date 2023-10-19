import dash  # Importar la biblioteca Dash para crear aplicaciones web interactivas
from dash import html  # Importa los componentes necesarios de la libreria de Dash
import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components
from dash.dependencies import Input, Output  # Importar las librerías necesarias de Dash dependencies para emplear los elementos de Input y Output

#importamos el frontend
from frontend.main import layout  # Importar la variable "layout" de la carpeta del frontend
from frontend.navegador.navegador import *  # Importar todo lo que se encuentra en el archivo navegador de la carpeta frontend

#importamos el backend
from backend.carta import cartaPlasticidad  # Importar la variable "cartaPlasticidad" de la carpeta del backend

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])  # Crear una instancia de la aplicación Dash
server = app.server  # Configurar el servidor de la aplicación para ser utilizado como página web
app.layout = layout  # Establecer el diseño de la aplicación utilizando el layout importado


@app.callback(  # Callback para mostrar texto basado en la opción seleccionada
    dash.dependencies.Output('texto-seleccionado', 'children'),  # Define la salida (componente que muestra el texto)
    dash.dependencies.Input('dropdown-opciones', 'value')  # Define la entrada (opción seleccionada en el menú desplegable)
)
def mostrar_texto(opcion_seleccionada):  # Crear una función para mostrar el texto de la opción que se seleccione del menú desplegable
    texto = {  # Se define las opciones seleccionadas con texto descriptivo
        'MH': "Suelo MH (Materiales de Alta Plasticidad): Este tipo de suelo tiene un alto índice de plasticidad y un alto límite líquido. "
              "Son suelos muy plásticos que pueden cambiar de forma significativamente bajo carga. Tienden a retener una cantidad considerable "
              "de agua, lo que los hace propensos a la expansión y contracción. Los suelos MH son comunes en áreas con alto contenido de arcilla. "
              "En la construcción, se deben tomar precauciones para evitar problemas de cimentación y estabilidad.",  # Para la opción "MH", se muestra la definición de ese suelo
        'CL': "Suelo CL (Materiales con Límite de Plasticidad Bajo): Este tipo de suelo tiene un bajo índice de plasticidad y un bajo límite líquido. "
              "Son suelos no plásticos y no retienen mucha agua. Los suelos CL son típicos en regiones con suelos arenosos o gravas. Son adecuados "
              "para la construcción de estructuras ligeras y no presentan problemas significativos de expansión o contracción.",  # Para la opción "CL", se muestra la definición de ese suelo
        'CH': "Suelo CH (Materiales de Alta Plasticidad): Los suelos CH tienen un alto índice de plasticidad y un alto límite líquido, lo que los "
              "hace muy plásticos y capaces de retener una gran cantidad de agua. Se encuentran en áreas con arcillas expansivas y son propensos a cambios "
              "volumétricos significativos con cambios de humedad. En la construcción, es importante tomar medidas para controlar la expansión y la contracción.",  # Para la opción "CH", se muestra la definición de ese suelo
        'ML': "Suelo ML (Materiales con Límite de Plasticidad Bajo): Estos suelos tienen un bajo índice de plasticidad y un bajo límite líquido. No son muy "
              "plásticos y retienen una cantidad limitada de agua. Los suelos ML son comunes en suelos que son una mezcla de arcilla y arena. Son adecuados "
              "para construcción de caminos y estructuras ligeras.",  # Para la opción "ML", se muestra la definición de ese suelo
        'NO EXISTE': "El punto no se encuentra en la carta de plasticidad."  # Para la opción "NO EXISTE", se muestra que el punto no se encuentra en la carta de plasticidad
    }
    return texto.get(opcion_seleccionada, "No se ha seleccionado una opción válida.")  # Regresa el mensaje respecto a la opción seleccionada, sino se encuentra se devuelve "No se ha seleccionado una opción válida." como un valor predeterminado.

@app.callback(  # Callback para cambiar el contenido de las pestañas
    Output('tab-content', 'children'),  # Define la salida (contenido de la pestaña)
    Input('tabs', 'active_tab')  # Define la entrada (pestaña activa)
)
def render_tab_content(active_tab):  # Crear una función para mostrar el texto de la tab seleccionada
    if active_tab == "tab-1":  # Define que si la tab-1 es seleccionada 
        return tab_como_funciona  # Devuelve el contenido de la tab seleccionada, está se desplega
    elif active_tab == "tab-2":  # Define que si la tab-2 es seleccionada 
        return tab_caracteristicas_suelo  # Devuelve el contenido de la tab seleccionada, está se desplega
    elif active_tab == "tab-3":  # Define que si la tab-3 es seleccionada 
        return tab_clasificacion_suelos  # Devuelve el contenido de la tab seleccionada, está se desplega

@app.callback(  # Callback para calcular la carta de plasticidad
    Output('salidaCartaPlasticidad', 'children'),  # Define la salida (componente que muestra la carta)
    Input('Limite_liquido', 'value'),  # Define la entrada (valor del límite líquido)
    Input('Indice_plasticidad', 'value')  # Define la entrada (valor del índice de plasticidad)
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):  # Crear una función para mostrar el contenido de la carta de plasticidad, con dos variables "Limite_liquido" y "Indice_plasticidad" 
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)  # Llama a la función cartaPlasticidad con los valores de Limite_liquido e Indice_plasticidad y almacena el resultado en encoded_image y messages.

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento de imagen utilizando los datos codificados que se generaron en la función cartaPlasticidad.
    messages_element = html.Label(messages)  # Crea un elemento de etiqueta utilizando los mensajes generados en la función cartaPlasticidad

    return html.Div([image_element, messages_element])  # Devuelve una estructura que contiene la imagen y los mensajes para mostrar en la interfaz.
    
if __name__ =='__main__':  # Comprueba si el script se está ejecutando como un programa independiente.
    app.run_server(debug=True)  # se inicia el servidor de Dash en modo de depuración (debug=True).
