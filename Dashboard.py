# %%Dash v2
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/daniyar135/supportapps-flam/main/SPRI.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/daniyar135/supportapps-flam/main/Dealer.csv')
app = Dash(__name__)
server = app.server

fig = px.scatter(df, y="Pass Rate", x="Courses Taken", color="Code", size="Courses Taken", trendline="ols")
fig1 = px.scatter(df1, y="pass_rate", x="courses_taken", color="Code", size="Number of Audits", trendline="ols")

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our Dealer Network and SPRI warehouses.
    '''),

    html.Div(children='''
        Hover over a dot to see which SPRI/Dealer it represents, number of courses taken, and average pass rate.
    '''),

    dcc.Graph(
        id='spri-graph',
        figure=fig
    ),

    dcc.Graph(
        id='dealer-graph',
        figure=fig1
    ),

    html.Div(children='''
        Adjust this slider for pass rate
    '''),

    dcc.Slider(
        df1['pass_rate'].min(),
        df1['pass_rate'].max(),
        step=None,
        value=df1['pass_rate'].max(),
        id='passrate-slider'
    )
])

@app.callback(
    Output('dealer-graph', 'figure'),
    Input('passrate-slider', 'value'))

def update_figure(selected_passrate):
    filtered_df = df1[df1.pass_rate <= selected_passrate]

    fig = px.scatter(filtered_df, x="courses_taken", y="pass_rate", color="Code", size="Number of Audits", trendline="ols",
                     log_x=True, size_max=55)
    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server()

# %%
