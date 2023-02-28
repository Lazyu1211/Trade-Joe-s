from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output,Input
from utill import get_data, get_ny, get_nj

def render(app):
    df = get_data()

    @app.callback(
    Output("pie_volume", component_property='children'),
    Input("states_dropdown",component_property='value')
    )

    def update_pie_chart(dropdown):
        filtered_data = df.query("state in @dropdown")
        fig = px.pie(filtered_data, values = 'store_count', names = "state", title = 'Stores Porportion')
        return html.Div(dcc.Graph(figure=fig),id="pie_volume")
    return html.Div(id="pie_volume")

def render1(app):
    df = get_ny()
    fig = px.pie(df, values = "city", names = df.index, title = 'Stores Counts by New York Cities')
    return html.Div(dcc.Graph(figure=fig),id="pie_volume1")

def render2(app):
    df = get_nj()
    fig = px.pie(df, values = "city", names =df.index, title="Stores Counts by New Jersey Cities")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume2")