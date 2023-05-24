
# https://dash.plotly.com/tutorial

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Initialize app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    
    # Title
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),

    # Horizontal line
    html.Hr(),

    # Text
    html.Div(
        className='row',
        children='My First App with Data, Graph, and Controls',
        style={
            'textAlign': 'center', 
            'color': 'blue', 
            'fontSize': 30
        }
    ),

    # Multiple choice (single answer)
    html.Div(
        className='row',
        children=[
            dcc.RadioItems(
                options=[
                    'pop',
                    'lifeExp',
                    'gdpPercap'
                ],
                value='lifeExp',
                inline=True,
                id='controls-and-radio-item'
            )
        ]
    ),
    
    # Two columns
    html.Div(
        className='row',
        children=[
            html.Div(
                className='six columns',
                children=[

                    # Table
                    dash_table.DataTable(
                        data=df.to_dict('records'),
                        page_size=11,
                        style_table={
                            'overflowX': 'auto'
                        }
                    )
                ]
            ),
            html.Div(
                className='six columns',
                children=[

                    # Bar chart
                    dcc.Graph(
                        figure={}, 
                        id='controls-and-graph'
                    )
                ]
            )
        ]
    ),

    # Dropdown
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),

    # Line chart
    dcc.Graph(id='graph-content')
])

# Interaction controls
@callback(
        
    # Bar chart figure
    Output(component_id='controls-and-graph', component_property='figure'),
    
    # Multiple choice input
    Input(component_id='controls-and-radio-item', component_property='value'),
)
def update_barchart(col_chosen):
    
    # Update bar chart
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

@callback(
        
    # Line chart figure    
    Output('graph-content', 'figure'),
    
    # Dropdown input    
    Input('dropdown-selection', 'value'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(value, col_chosen):
    
    # Update line chart
    dff = df[df.country==value]
    return px.line(dff, x='year', y=col_chosen)

if __name__ == '__main__':
    app.run_server(debug=True)
