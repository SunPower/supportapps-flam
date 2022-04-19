# %%Dash v2
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/daniyar135/flam/main/Training%20Hours%20VS%20Pass%20Rate.csv')
app = Dash(__name__)
server = app.server

fig = px.bar(df, y="Pass Rate", x="Group Courses Taken", color="Warehouse Name", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our SPRI warehouses
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server()
