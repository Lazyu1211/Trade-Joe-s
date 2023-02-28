from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_list

def render(app):
    list_states = get_list()
    all_states = [{'label':i,'value':i} for i in list_states]
    @app.callback(
    Output(component_id='states_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_bedroom(n):
        return list_states

    return html.Div(
        children=[
            html.H6("Select States"),
            dcc.Dropdown(
                options=all_states,
                multi=True,
                id = "states_dropdown",
                value= "CA"
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )