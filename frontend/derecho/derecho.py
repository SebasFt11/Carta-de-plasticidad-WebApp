from dash import html, dcc  # Importar los componentes necesarios de la libreria de Dash
import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components

derecho = dbc.Container(  # Se crea un contenedor de Dash que señala los elementos que contendrán la parte derecha de la página.
    [
        html.Div(
            [
                html.H2('Indice de plasticidad '),  # Crear título de nivel 2 de la sección.
                html.Label('Limite liquido '),  # Etiqueta para describir el punto deslizante del Límite Líquido.
                dcc.Slider(  # Punto deslizante para seleccionar el valor del Límite Líquido.
                    id='Limite_liquido',  # Asignar un ID al punto deslizante.
                    min=0,  # Valor mínimo permitido.
                    max=100,  # Valor máximo permitido.
                    value=55,  # Valor inicial del punto deslizante.
                    step=1,  # Incremento entre valores permitidos.
                    marks={i: str(i) for i in range(0, 101, 10)}  # Marcas en el punto deslizante para valores específicos.
                ),
                html.Label('Indice de plasticidad'), # Etiqueta para describir el punto deslizante del Índice de Plasticidad.
                dcc.Slider(
                    id='Indice_plasticidad',  # Asignar un ID al punto deslizante.
                    min=0,  # Valor mínimo permitido.
                    max=60,  # Valor máximo permitido.
                    value=20,   # Valor inicial del punto deslizante.
                    step=1,  # Incremento entre valores permitidos.
                    marks={i: str(i) for i in range(0, 61, 10)}  # Marcas en el punto deslizante para valores específicos.
                ),

                # dcc.Input(id = 'Limite_liquido', value = 55 , type = 'number'),
                # dcc.Input(id = 'Indice_plasticidad', value = 5 , type = 'number'),
                html.Div(id='salidaCartaPlasticidad')   # Un elemento div que se utilizará para mostrar la salida de la carta de plasticidad.
            ]
        ),
    ],
    style={'background-color':'white'}  # Establece el color de fondo del contenedor en blanco.
)


