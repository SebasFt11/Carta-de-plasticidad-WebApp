import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components
from  dash import html, dcc  # Importa los componentes necesarios de la libreria de Dash

izquierdo = dbc.Container([  # Se crea un contenedor de Dash que señala los elementos que contendrán la parte izquierda de la página.
    dcc.Dropdown(  # Crear un menú desplegable para seleccionar una opción.
        id='dropdown-opciones',  #   # Asignar un ID al menú desplegable.
        options=[  # Opciones del menú desplegable.
            {'label': 'MH', 'value': 'MH'},  # Se especifica como va a aparecer cada opción, en este caso es el suelo de tipo MH.
            {'label': 'CL', 'value': 'CL'},  # Se especifica como va a aparecer cada opción, en este caso es el suelo de tipo CL.
            {'label': 'CH', 'value': 'CH'},  # Se especifica como va a aparecer cada opción, en este caso es el suelo de tipo CH.
            {'label': 'ML', 'value': 'ML'},  # Se especifica como va a aparecer cada opción, en este caso es el suelo de tipo ML.
            {'label': 'NO EXISTE', 'value': 'NO EXISTE'}  # Se especifica como va a aparecer cada opción, en este caso es NO EXISTE.
        ],
        value='MH'  # Opción predeterminada
    ),
    html.Div(id='texto-seleccionado', className="p-4"),  # Con el 'id' permite actualizar el contenido dinámicamente.
])