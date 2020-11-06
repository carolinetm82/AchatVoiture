# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('carData.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# 
app.layout = html.Div([
    html.H1('Comment acheter sa voiture', style={'textAlign': 'center'}),

    dcc.Graph(id='graph-with-slider'),

    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].min(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.Year == selected_year]

    fig = px.scatter(filtered_df, x="Kms_Driven", y="Selling_Price", 
                     color="Transmission")

    fig.update_layout(transition_duration=1000)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)