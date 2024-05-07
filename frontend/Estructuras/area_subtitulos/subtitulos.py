import dash
from dash import html, dcc
import dash_bootstrap_components as dbc 
import base64
from dash.dependencies import Input, Output

from frontend.Estructuras.DatosCR.CanalR import variableCR
from frontend.Estructuras.DatosCT.CanalT import variableCT
from frontend.Estructuras.DatosCC.CanalC import variableCC
from frontend.Estructuras.DatosCTR.CanalTR import variableCTR

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Cargar la imagen como un archivo binario
with open('frontend/Imagenes/Canal inicio.png', 'rb') as img_file:
    encoded1_img = base64.b64encode(img_file.read()).decode('ascii')

with open('frontend/Imagenes/Formulascanales.png', 'rb') as img_file2:
    encoded2_img = base64.b64encode(img_file2.read()).decode('ascii')

# Contenedor de los botones en una sola fila
variableB = html.Div([

    dcc.Tabs([
        dcc.Tab(label='INICIO',
            children=[
                html.Div([html.P("El estudio de las propiedades hidráulicas de la sección transversal posee singular importancia puesto que dicha sección define muchas de las características hidráulicas del flujo.",style={'background-color':'gold'}),
                          html.Br(),
                          html.H3("PROPIEDADES GEOMÉTRICAS DE LOS CANALES",style={'textAlign': 'center'}),
                          html.Br(),
                          html.Img(src=f'data:image/png;base64,{encoded1_img}', style={'width': '40%', 'height': 'auto','textAlign': 'center'}),
                          html.H6("La sección transversal de un canal natural es generalmente de forma muy irregular y varia de un lugar a otro, desde aproximadamente una parábola hasta aproximadamente un trapecio.",style={'textAlign': 'justify'}),
                          html.Br(),
                          html.H6("Los canales artificiales usualmente se diseñan con formas geométricas regulares (prismáticos), un canal construido con una sección transversal invariable y una pendiente de fondo constante se conoce como canal prismático. El término sección de canal se refiere a la sección transversal de un canal tomado en forma perpendicular a la dirección del flujo, las secciones más comunes son las siguientes:",style={'textAlign': 'justify'}),
                          html.Br(),
                          html.H6("Sección rectangular:  Debido a que el rectángulo tiene lados verticales, por lo general se utiliza para canales construidos con materiales estables, acueductos de madera, para canales excavados en roca y para canales revestidos.",style={'textAlign': 'justify'}),
                          html.H6("Sección trapezoidal:  Se usa en canales de tierra debido a que proveen las pendientes necesarias para estabilidad, y en canales revestidos.",style={'textAlign': 'justify'}),
                          html.H6("Sección circular: El círculo es la sección más común para alcantarillados y alcantarillas de tamaños pequeño y mediano",style={'textAlign': 'justify'}),
                          html.H6("Sección triangular: Se usa para cunetas revestidas en las carreteras, también en canales de tierra pequeños, fundamentalmente por facilidad de trazo. También se emplean revestidas, como alcantarillas de las carreteras.",style={'textAlign': 'justify'}),
                          html.Br(),
                          html.Img(src=f'data:image/png;base64,{encoded2_img}', style={'width': '40%', 'height': 'auto','textAlign': 'center'}),
                          html.Br(),
                          html.Br(),
                          html.Br(),

                ])
                 ]),
        dcc.Tab(label='RECTANGULAR',
                children=[
                    html.Div(variableCR,style={'background-color':'lightseagreen'})

                ]),
        dcc.Tab(label='TRAPEZOIDAL',
                children=[
                    html.Div(variableCT,style={'background-color':'mediumturquoise'})

                ]),
        dcc.Tab(label='CIRCULAR',
                children=[
                    html.Div(variableCC,style={'background-color':'turquoise'})


                ]),
        dcc.Tab(label='TRIANGULAR',
                children=[
                    html.Div(variableCTR,style={'background-color':'paleturquoise'})

                ]),
    ])

])  

