from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data, get_nj

def render(app):
    df = get_data()

    @app.callback(
        Output("line_volume", component_property='children'),
        Input("states_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("state in @dropdown")
        fig = px.line(
                filtered_data,
                x="state",
                y="population",
                title="Total Population of States")
        return html.Div(dcc.Graph(figure=fig),id="line_volume")
    return html.Div(id="line_volume")

