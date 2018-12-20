import plotly.graph_objs as go
import pandas as pd

dfPokemon = pd.read_csv('dataPokemon.csv')

ListFunc = {
    "bar" : go.Bar,
    "box" : go.Box,
    "violin" : go.Violin
}


def getPlot(jenis):
    return[ListFunc[jenis](
                x=dfPokemon['Generation'],
                y=dfPokemon['Total'],
                text=dfPokemon['Type 2'],
                opacity=0.7,
                name='Total'
            ),
                ListFunc[jenis](
                x=dfPokemon['Generation'],
                y=dfPokemon['Attack'],
                text=dfPokemon['Type 2'],
                opacity=0.7,
                name='Attack'
            )]