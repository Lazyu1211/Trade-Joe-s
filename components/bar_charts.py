from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data

def render(app):
    df = get_data()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("states_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("state in @dropdown")
        fig = px.bar(
                filtered_data,
                x="state",
                y="median_4_family_income",
                title="Four people family Median income by States")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")

def render1(app):
    df = get_data()

    @app.callback(
        Output("bar_volume1", component_property='children'),
        Input("states_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("state in @dropdown")
        fig = px.bar(
                filtered_data,
                x="state",
                y="density",
                title="Population Density by States")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume1")

