# %%Dash v2
from logging import PlaceHolder
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
fig = px.scatter(df1, x="Number of Inspections", y="pass_rate", color="Name", trendline="ols")

app.layout = html.Div(children=[
    html.H1(children='FLAM Dashboard'),

    html.Div(children='''
        Visualizing data from our Dealer Network and SPRI warehouses.
    '''),

    html.Div(children='''
        Hover over a dot to see which SPRI/Dealer it represents, number of courses taken, number of audits, and average pass rate.
    '''),

    html.Div(children='''
        Choose number of courses below:
    '''),

    dcc.Dropdown(
        style = {'text-align': 'center', 'font-size': '18px', 'width': '120px'},
        options=df1['courses_taken'].unique(),
        value = 1, 
        id='courses-dropdown',
        placeholder="Select # of courses taken",
        clearable=False),
    html.Div(id='dd-output-container'),

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
    [Input('passrate-slider', 'value'),
    Input('courses-dropdown', 'value')])

def update_figure(pass_rate, courses_taken):

    filtered_df = df1[df1.pass_rate <= pass_rate] and df1[df1.courses_taken == courses_taken]
    fig = px.scatter(filtered_df, x="Number of Inspections", y="pass_rate", color="Name", trendline="ols")
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server()

# %%
