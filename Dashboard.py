# %%Dash v2
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

#df = pd.read_csv('https://raw.githubusercontent.com/daniyar135/supportapps-flam/main/SPRI.csv')
#df1 = pd.read_csv('https://raw.githubusercontent.com/daniyar135/supportapps-flam/main/Dealer.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/daniyar135/supportapps-flam/main/All.csv')
app = Dash(__name__)
server = app.server

#fig = px.scatter(df, y="Pass Rate", x="Courses Taken", color="Code", size="Courses Taken", trendline="ols")
#fig1 = px.scatter(df1, y="pass_rate", x="courses_taken", color="Code", size="Number of Audits", trendline="ols")
fig = px.scatter(df1, y="pass_rate", x="courses_taken", color="Name", size="Number of Inspections", trendline="ols")

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our Dealer Network and SPRI warehouses.
    '''),

    html.Div(children='''
        Hover over a dot to see which SPRI/Dealer it represents, number of courses taken, and average pass rate.
    '''),

    dcc.Graph(
        id='all-graph',
        figure=fig
    ),

    # dcc.Graph(
    #     id='spri-graph',
    #     figure=fig
    # ),

    html.Div(children='''
        Adjust this slider for pass rate
    '''),

    dcc.Slider(
        df1['pass_rate'].min(),
        df1['pass_rate'].max(),
        step=None,
        value=df1['pass_rate'].max(),
        tooltip={"placement": "bottom", "always_visible": True},
        id='passrate-slider'
    )
])

@app.callback(
    Output('all-graph', 'figure'),
    Input('passrate-slider', 'value'))

def update_figure(selected_passrate):
    filtered_df = df1[df1.pass_rate <= selected_passrate]

    fig = px.scatter(filtered_df, x="courses_taken", y="pass_rate", color="Name", size="Number of Inspections", trendline="ols")
    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server()

# %%
