import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from categoryplot import dfPokemon, getPlot
from dash.dependencies import Input, Output


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe.iloc[i][col])) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )



color_set = ['#000000' , '#FCE63D']

app = dash.Dash(__name__)

app.title = 'Pokemon'

app.layout = html.Div(children=[
    html.H1(children='Dashboard Pokemon' , className = 'titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Pokemon DataSet', value='tab-1', children=[
            html.Div([
                html.H1('Data Pokemon' , className = 'h1'),
                generate_table(dfPokemon)
            ])
        ]),
        dcc.Tab(label='Scatter Plot' , value='tab-2' , children=[
            html.Div([
                html.H1('Scatter Plot Pokemon' , className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data' : [
                            go.Scatter(
                                x=dfPokemon[dfPokemon['Legendary'] == col]['Attack'],
                                y=dfPokemon[dfPokemon['Legendary'] == col]['Defense'],
                                mode='markers',
                                marker=dict(color = color_set[i] , size=10, line={'width' : 0.5, 'color' : 'white'}), 
                                name=str(col) 
                                
                            ) for col, i in zip(dfPokemon['Legendary'].unique() , range(2))
                        ],
                        'layout' : go.Layout(
                            xaxis={'title' : 'Attack'},
                            yaxis={'title' : 'Defense'},
                            margin={'l' : 40, 'b' : 40 , 't' : 10, 'r' : 10},
                            hovermode='closest'
                        )
                    }
                )
            ])
        ]),
        dcc.Tab(label='Categorical Plot', value='tab-3', children=[
            html.Div([
                html.H1('Categorical Plot' , className = 'h1'),
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                        id='jenisPlot',
                        options=[{'label': i.capitalize(), 'value': i} for i in ['bar','box','violin']],
                        value='bar')
                    ] , className='col-xs-4')
                ],className='row'),
                dcc.Graph(
                    id='categoricalPlot',
                    # figure={
                    #     'data' :[
                    #         go.Bar(
                    #             x=dfPokemon['Generation'],
                    #             y=dfPokemon['Total'],
                    #             text=dfPokemon['Type 2'],
                    #             opacity=0.7,
                    #             name='Total'
                    #         ),
                    #          go.Bar(
                    #             x=dfPokemon['Generation'],
                    #             y=dfPokemon['Attack'],
                    #             text=dfPokemon['Type 2'],
                    #             opacity=0.7,
                    #             name='Attack'
                    #         )
                    #     ],
                    #     'layout' : go.Layout(
                    #         xaxis = {'title' : 'Generation'},
                    #         yaxis = {'title' : 'Total Stats'},
                    #         margin={'l' : 40, 'b' : 40 , 't' : 10, 'r' : 10},
                    #         # legend= {'x' : 0 , 'y' : 1},
                    #         hovermode='closest'
                    #     )
                    # }
                )
            ])
        ])

    ], style={
        'fontFamily' : 'system-ui'
    }, content_style = {
        'fontFamily' : 'Arial',
        'borderBottom' : '1px solid #d6d6d6',
        'borderRight' : '1px solid #d6d6d6',
        'borderLeft ' : '1px solid #d6d6d6',
        'padding' : '44px'
    })
] , style = {
    'maxWidth' : '1200px',
    'margin' : '0 auto'
})

@app.callback(
    Output(component_id='categoricalPlot', component_property='figure'),
    [Input(component_id='jenisPlot', component_property='value')])
def update(jenisPlot):
        return {
            "data" : getPlot(jenisPlot),
            'layout' : go.Layout(
                    xaxis = {'title' : 'Generation'},
                    yaxis = {'title' : 'Total Stats'},
                    margin={'l' : 40, 'b' : 40 , 't' : 10, 'r' : 10},
                    # legend= {'x' : 0 , 'y' : 1},
                    hovermode='closest')
                }  


if __name__ == '__main__':
    # run server on port 1997
    # debug=True for auto restart if code edited
    app.run_server(debug=True, port=1997)


    # Bikin Dropdown Baru buat menentukan X Axis yang ditambah cuma callback input, terus di func update di tambah parameter dan getplot juga