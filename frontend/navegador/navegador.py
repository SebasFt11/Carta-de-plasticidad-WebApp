import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components
from dash import html  # Importa los componentes necesarios de la libreria de Dash

tab_como_funciona = html.Div([  # Contenido de la pestaña "Cómo funciona"
    html.H2("¿Cómo funciona la caracterización del suelo?"),  # Crear un título de nivel 2
    html.P("¡Bienvenido a nuestra página web de caracterización de suelos! Aquí te explicaremos cómo utilizar "
           "nuestra herramienta para caracterizar diferentes tipos de suelo a través del índice de plasticidad y el límite líquido."),  # Crear un párrafo explicativo

    html.H3("Paso 1: Entendiendo las Variables"),  # Crear un título de nivel 3
    html.P("Para comenzar, es importante comprender las dos variables clave que utilizamos para caracterizar el suelo:"),  # Crear un párrafo explicativo

    html.Ul([  # Crear una lista con viñetas
        html.Li("Índice de Plasticidad: Esta variable describe la diferencia entre el límite líquido y el límite plástico del suelo. "
                 "Es una medida de la plasticidad del suelo y su capacidad para retener agua."),  # Crear contenido de cada viñeta
        html.Li("Límite Líquido: El límite líquido es el contenido de humedad en el suelo en el que se comporta como un líquido y fluye. "
                 "Es una medida importante para comprender la plasticidad del suelo.")  # Crear contenido de cada viñeta
    ]),

    html.H3("Paso 2: Conoce las Características del Suelo"),  # Crear un título de nivel 3
    html.P("Si deseas obtener una comprensión más profunda de estas características del suelo, te invitamos a explorar la pestaña "
           "'Características del Suelo'. Allí, encontrarás información detallada sobre el índice de plasticidad, el límite líquido "
           "y cómo afectan la caracterización del suelo."),  # Crear un párrafo explicativo

    html.H3("Paso 3: Caracterizando el Suelo"),  # Crear un título de nivel 3
    html.P("Una vez que hayas comprendido las variables, ve a la pestaña 'Caracterización de Suelos'. Allí, pon los valores "
           "del índice de plasticidad y el límite líquido del suelo que deseas caracterizar."),  # Crear un párrafo explicativo

    html.H3("Paso 4: Resultado de la Caracterización"),  # Crear un título de nivel 3
    html.P("Nuestra página web determinará la clasificación del suelo en función de los valores que ingresaste y te mostrará el resultado. "
           "Si es necesario, podrás ajustar los valores para obtener una caracterización precisa del suelo."),  # Crear un párrafo explicativo

    html.P("¡Así de fácil es caracterizar el suelo utilizando nuestra herramienta! Ahora, puedes explorar la pestaña 'Características del Suelo' "
           "para obtener más información sobre las variables y cómo afectan a la caracterización."),  # Crear un párrafo explicativo
])

tab_caracteristicas_suelo = html.Div([  # Contenido de la pestaña "Características del suelo"
    html.H2("Características del Suelo"),  # Crear un título de nivel 2
    html.P("Para comprender la caracterización del suelo y su importancia, es esencial conocer tres variables fundamentales. "
           "A continuación, te proporcionamos información detallada sobre estas características y cómo afectan la clasificación de suelos."),  # Crear un párrafo explicativo

    html.H3("Carta de Plasticidad"),  # Crear un título de nivel 3
    html.P("La carta de plasticidad es una herramienta esencial para evaluar las propiedades del suelo en términos de su plasticidad. "
           "Esta carta relaciona el límite líquido con el índice de plasticidad y se utiliza para clasificar el suelo en diferentes grupos. "
           "Comprender la carta de plasticidad es crucial para determinar las características del suelo y su comportamiento."),  # Crear un párrafo explicativo

    html.H3("Límite Líquido"),  # Crear un título de nivel 3
    html.P("El límite líquido es el contenido de humedad en el suelo en el que se comporta como un líquido y fluye. "
           "Este valor es fundamental para evaluar la plasticidad del suelo. Los suelos con un límite líquido más alto tienden a ser "
           "más plásticos, lo que significa que pueden cambiar de forma y retener agua con facilidad."),  # Crear un párrafo explicativo

    html.H3("Índice de Plasticidad"),  # Crear un título de nivel 3
    html.P("El índice de plasticidad se calcula restando el límite líquido al límite plástico. Este índice proporciona una medida "
           "de la plasticidad del suelo. Los suelos con un índice de plasticidad más alto son más plásticos y, por lo tanto, "
           "tienen la capacidad de cambiar de forma y retener agua con facilidad. Entender este índice es crucial para la caracterización "
           "y clasificación del suelo."),  # Crear un párrafo explicativo

    html.H2("Importancia de la Clasificación del Suelo"),  # Crear un título de nivel 2
    html.P("La clasificación del suelo desempeña un papel crucial en diversas aplicaciones, incluyendo la construcción, la ingeniería civil, "
           "la agricultura y la protección del medio ambiente. Comprender las características del suelo, como la carta de plasticidad, el "
           "límite líquido y el índice de plasticidad, permite tomar decisiones informadas sobre cómo utilizar y gestionar el suelo de manera efectiva. "
           "Nuestra página web te proporciona una herramienta precisa y sencilla para llevar a cabo esta caracterización y clasificación de suelos.")  # Crear un párrafo explicativo
])


tab_clasificacion_suelos = dbc.Container([  # Contenido de la pestaña "Clasificación de suelos"
    html.H2("Clasificación de suelos"),  # Crear un título de nivel 2
    html.P("Una vez entendido cómo funciona nuestra página web, ya puedes iniciar a clasificar el suelo que tengas, seleccionando " 
           "los valores de las variables que se adecuen al suelo a clasificar. Una vez obtengas el tipo de suelo, en la parte derecha podras saber que caracteristicas tiene tu suelo.")  # Crear un párrafo explicativo
])

tab_active_style = {"background-color": "blue", "color": "white"}  # Crear estilos para las pestañas
tab_inactive_style = {"background-color": "green", "color": "white"}  # Crear estilos para las pestañas

navegador = dbc.Container([  # Se crea un contenedor de Dash que señala los elementos que contendrán la parte del navegador de la página.
    dbc.Tabs(  # Crear las pestañas con Tabs
        [
            dbc.Tab(label="¿Cómo funciona?", tab_id="tab-1", style = {'height' : '5px','background-color' : 'white', 'color' : 'black', 'border-top' : '5px solid white', 'border-right' : '1px solid white' }),  # Crear la primera pestaña con el texto "¿Cómo funciona?" y establecer su identificación en "tab-1" y estilo del tab
            dbc.Tab(label="Caracteristicas del suelo", tab_id="tab-2",style = {'background-color' : 'white', 'border-top' : '5px solid white', 'border-right' : '1px solid white'}),  # Crear la primera pestaña con el texto "Caracteristicas del suelo" y establecer su identificación en "tab-2" y estilo del tab
            dbc.Tab(label="¿Qué suelo tengo?", tab_id="tab-3",style = {'background-color' : 'white', 'border-top' : '5px solid white'})  # Crear la primera pestaña con el texto "¿Qué suelo tengo?" y establecer su identificación en "tab-3" y estilo del tab
        ],
        id="tabs",  # Asignar un ID al componente de pestañas
        active_tab="tab-1",  # Pestaña activa por defecto.
    ),

    html.Div(id="tab-content", className="p-4"),  # Mostrar el contenido de las pestañas.
])
        