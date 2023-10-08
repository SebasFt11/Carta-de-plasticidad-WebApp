import dash
import dash_bootstrap_components as dbc
from dash import html

# Contenido de la pestaña "Cómo funciona"
tab_como_funciona = html.Div([
    html.H2("¿Cómo funciona la clasificación de suelos?"),
    html.P("¡Bienvenido a nuestra página web de clasificación de suelos! Aquí te explicaremos cómo utilizar "
           "nuestra herramienta para clasificar diferentes tipos de suelo de manera sencilla y precisa."),

    html.H3("Paso 1: Entendiendo las Variables"),
    html.P("Para comenzar, es importante comprender las tres variables clave que utilizamos para clasificar el suelo:"),

    html.Ul([
        html.Li("Permeabilidad: Esta variable describe la capacidad del suelo para permitir el paso del agua. "
                 "Puedes elegir entre 'Alta', 'Media' o 'Baja'."),
        html.Li("Cantidad de Materia Orgánica: Esta variable indica la cantidad de materia orgánica presente en el suelo. "
                 "Las opciones son 'Altísima', 'Mediana' o 'Bajísima'."),
        html.Li("Textura del Suelo: La textura se refiere a la sensación táctil del suelo. Puedes seleccionar 'Liso', 'Rugoso' "
                 "o 'Fandoso'.")
    ]),

    html.H3("Paso 2: Conoce las Características del Suelo"),
    html.P("Si deseas obtener una comprensión más profunda de estas características del suelo, te invitamos a explorar la pestaña "
           "'Características del Suelo'. Allí, encontrarás información detallada sobre cada variable y cómo afecta a la clasificación."),

    html.H3("Paso 3: Clasificando el Suelo"),
    html.P("Una vez que hayas comprendido las variables, ve a la pestaña 'Clasificación de Suelos'. Allí, selecciona las "
           "opciones que mejor describan el suelo que deseas clasificar. Después, haz clic en el botón 'Clasifica'."),

    html.H3("Paso 4: Resultado de la Clasificación"),
    html.P("Nuestra página web determinará el tipo de suelo en función de tus selecciones y te mostrará el resultado. "
           "Si es necesario, podrás ajustar las opciones y volver a hacer clic en 'Clasifica' para obtener una clasificación "
           "precisa del suelo."),

    html.P("¡Así de fácil es clasificar el suelo utilizando nuestra herramienta! Ahora, puedes explorar la pestaña 'Características del Suelo' "
           "para obtener más información sobre las variables y cómo afectan a la clasificación."),
])

# Contenido de la pestaña "Características del suelo"
tab_caracteristicas_suelo = html.Div([
    html.H2("Características del Suelo"),
    html.P("Las características del suelo son fundamentales para comprender su comportamiento y cómo afecta a diferentes "
           "procesos naturales y actividades humanas. A continuación, explicaremos en detalle tres de las características "
           "más importantes que utilizamos para clasificar el suelo en nuestra página web."),

    html.H3("Permeabilidad del Suelo"),
    html.P("La permeabilidad del suelo se refiere a su capacidad para permitir que el agua lo atraviese. Esta característica "
           "es esencial, ya que afecta directamente a la retención de agua en el suelo y su capacidad para drenar. "
           "Las tres categorías de permeabilidad que consideramos son:"),
    html.Ul([
        html.Li("Alta: El suelo permite que el agua fluya fácilmente a través de él."),
        html.Li("Media: El suelo retiene algo de agua pero también permite el drenaje."),
        html.Li("Baja: El suelo retiene la mayoría del agua y tiene un drenaje limitado.")
    ]),
    html.P("La permeabilidad es crucial para la agricultura, la construcción y la gestión del agua subterránea, y juega un papel "
           "fundamental en la clasificación de suelos."),
    
    html.H3("Textura del Suelo"),
    html.P("La textura del suelo se refiere a cómo se siente al tacto y se relaciona con el tamaño de las partículas de suelo. "
           "Las diferentes texturas afectan la capacidad del suelo para retener nutrientes y agua. Las opciones que consideramos son:"),
    html.Ul([
        html.Li("Franco: Suelo equilibrado con partículas de diferentes tamaños."),
        html.Li("Turboso: Suelo con partículas muy pequeñas y finas."),
        html.Li("Pedregoso: Suelo con presencia significativa de piedras o fragmentos rocosos."),
        html.Li("Arenoso: Suelo con partículas grandes y una capacidad limitada para retener agua."),
        html.Li("Arcilloso: Suelo con partículas muy finas y una alta capacidad para retener agua y nutrientes.")
    ]),
    html.P("La textura del suelo es esencial para la agricultura, la jardinería y la gestión de tierras, ya que influye en la retención "
           "de agua y la disponibilidad de nutrientes para las plantas."),
    
    html.H3("Cantidad de Materia Orgánica"),
    html.P("La cantidad de materia orgánica en el suelo se refiere a la cantidad de residuos orgánicos descompuestos presentes en el suelo. "
           "Estos residuos enriquecen el suelo con nutrientes y mejoran su estructura. Las tres categorías que consideramos son:"),
    html.Ul([
        html.Li("Alto: Suelo rico en materia orgánica, con un alto contenido de nutrientes."),
        html.Li("Medio: Suelo con una cantidad moderada de materia orgánica."),
        html.Li("Bajo: Suelo con poco contenido de materia orgánica y nutrientes limitados.")
    ]),
    html.P("La cantidad de materia orgánica influye en la fertilidad del suelo y su capacidad para sostener la vida vegetal. "
           "Es un factor clave en la clasificación de suelos."),

    html.H2("Importancia de la Clasificación del Suelo"),
    html.P("La clasificación del suelo es esencial para una variedad de aplicaciones, incluyendo la agricultura, la construcción, "
           "la gestión del agua y la protección del medio ambiente. Al comprender las características del suelo y cómo se relacionan "
           "con sus propiedades, podemos tomar decisiones informadas sobre cómo utilizar y gestionar la tierra de manera efectiva. "
           "Nuestra página web te ayuda a clasificar el suelo de manera precisa y sencilla para facilitar estas decisiones.")
])

# Contenido de la pestaña "Clasificación de suelos"
tab_clasificacion_suelos = dbc.Container([
    html.H2("Clasificación de suelos"),
    html.P("Una vez entendido cómo funciona nuestra página web, ya puedes iniciar a clasificar el suelo que tengas, seleccionando " 
           "las opciones de las siguientes variables, que se adecuen mejor al suelo a clasificar.")
])

tab_active_style = {"background-color": "blue", "color": "white"}
tab_inactive_style = {"background-color": "green", "color": "white"}

navegador = dbc.Container([
    dbc.Tabs(
        [
            dbc.Tab(label="¿Cómo funciona?", tab_id="tab-1", style = {'height' : '5px','background-color' : 'white', 'color' : 'black', 'border-top' : '5px solid white', 'border-right' : '1px solid white' }),
            dbc.Tab(label="Caracteristicas del suelo", tab_id="tab-2",style = {'background-color' : 'white', 'border-top' : '5px solid white', 'border-right' : '1px solid white'}),
            dbc.Tab(label="¿Qué suelo tengo?", tab_id="tab-3",style = {'background-color' : 'white', 'border-top' : '5px solid white'})
        ],
        id="tabs",
        active_tab="tab-1",
    ),

    html.Div(id="tab-content", className="p-4"),
])
        