import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Cargar el dataset
file_path = '/home/Loboguerra/app/Pokemon.csv'
pokemon_df = pd.read_csv(file_path)

# Verificar los nombres de las columnas
print(pokemon_df.columns)

# Inicializar la app Dash
app = dash.Dash(__name__)

# Layout de la app
app.layout = html.Div([
    html.H1('Dashboard de Análisis de Pokémon'),
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Distribución de Tipos', children=[
            dcc.Graph(id='bar-plot')
        ]),
        dcc.Tab(label='Estadísticas por Generación', children=[
            dcc.Dropdown(
                id='stat-dropdown',
                options=[{'label': stat, 'value': stat}
                         for stat in ['HP', 'Atk', 'Def', 'Spa', 'Spd', 'Spe']],
                value='HP'
            ),
            dcc.Graph(id='box-plot')
        ]),
        dcc.Tab(label='Matriz de Correlación', children=[
            dcc.Graph(id='heatmap')
        ])
    ])
])

# Callbacks para actualizar los gráficos


@app.callback(
    Output('bar-plot', 'figure'),
    Input('tabs', 'value')
)
def update_bar_plot(tab):
    type_counts = pokemon_df['Type 1'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig = px.bar(type_counts, x='Type', y='Count',
                 title='Distribución de Tipos de Pokémon')
    return fig


@app.callback(
    Output('box-plot', 'figure'),
    Input('stat-dropdown', 'value')
)
def update_box_plot(stat):
    fig = px.box(pokemon_df, x='Generation', y=stat,
                 title=f'{stat} por Generación')
    return fig


@app.callback(
    Output('heatmap', 'figure'),
    Input('tabs', 'value')
)
def update_heatmap(tab):
    stats = ['HP', 'Atk', 'Def', 'Spa', 'Spd', 'Spe']
    corr_matrix = pokemon_df[stats].corr()
    fig = px.imshow(
        corr_matrix, title='Matriz de Correlación entre Estadísticas')
    return fig


# Ejecutar la app
if __name__ == '__main__':
    app.run_server(debug=True)
