# %%Dash v2
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/daniyar135/flam/main/Training%20Hours%20VS%20Pass%20Rate.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/daniyar135/flam/main/Training%20Hours%20VS%20Pass%20Rate%20Dealer.csv')
app = Dash(__name__)
server = app.server

fig = px.scatter(df, y="Pass Rate", x="Group Courses Taken", color="Warehouse Name", size="Group Courses Taken")
fig1 = px.scatter(df1, y="Pass Rate", x="Courses Taken", color="Dealer Name", size="Courses Taken")

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our Dealer Network and SPRI warehouses
    '''),

    html.Div(children='''
        Hover over a dot to see which SPRI/Dealer it represents, number of courses taken, and average pass rate
    '''),

    dcc.Graph(
        id='spri-graph',
        figure=fig
    ),

    dcc.Graph(
        id='dealer-graph',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server()

# %%
