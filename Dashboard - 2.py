# %%Dash v2
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

df1 = pd.read_csv('https://raw.githubusercontent.com/daniyar135/icebreaker/master/Training Hours VS Pass Rate.csv')
app = Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our longest SunVault related calls. The longer the call, the bigger the shape.
    '''),
    html.Div(children='''
        Use the slider at the bottom to see each week's longest calls that had silences > 2 minutes.
    '''),

    dcc.Graph(id='graph-with-slider'),

    dcc.Slider(
        df1['week'].min(),
        df1['week'].max(),
        step=None,
        value=df1['week'].min(),
        marks={str(week): str(week) for week in df1['week'].unique()},
        id='week-slider'
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('week-slider', 'value'))
def update_figure(selected_week):
    filtered_df = df1[df1.week == selected_week]

    fig = px.scatter(filtered_df, x="Number of silences", y="Call duration", size="Call duration", color="Recording ID",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server()
# %%
