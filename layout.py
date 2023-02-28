from dash import Dash,html
import dash_bootstrap_components as dbc
from components import dropdown, bar_charts, pie_charts, line_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_LOyzvzkUfgcQsAVFd7kfmLLQErKC4m5qRQ&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-1CeZLjaoJuDeaPJecQzi9GAKfjbeg9bKeA&usqp=CAU"
image_path2 =  ""
def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="✨✨✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Trade Joe's Stores Analysis", className="header-title"
              ),
        html.P(
                "Base on the dataset we can analysis what affects the locations of Trade Joe's Stores!!!🔥🔥🔥✨✨✨",
                className="header-description",
                ),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path2),
        dropdown.render(app)
    
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(pie_charts.render(app),lg=6),
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(line_charts.render(app),lg=6),
            dbc.Col(bar_charts.render1(app),lg=6),
            dbc.Col(pie_charts.render1(app),lg=6),
            dbc.Col(pie_charts.render2(app),lg=6)
            
        ],className="mt-4")
    ])