import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd 
import numpy as np


row_header = html.Div(
    [
        dbc.Row(dbc.Col(html.H1("Network"),style={"color":"#0D1E2E","textAlign":"center","paddingTop":30})),  
    ]
)


kpis = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card( 
                        [
                            dbc.CardBody(html.H1("test", style={"textAlign":"center", "color":"green"})),
                            dbc.CardFooter(html.P("test", style={"minHeight":"50px"}))
                        ]
                    )),
                    dbc.Col(dbc.Card(
                        [
                            dbc.CardBody(html.H1("test", style={"textAlign":"center","color":"#ff9933"})),
                            dbc.CardFooter(html.P("test"))
                        ]
                    )),
                    dbc.Col(dbc.Card(
                        [
                            dbc.CardBody(html.H1("100 %", style={"textAlign":"center", "color":"green"})),
                            dbc.CardFooter(html.P("test", style={"minHeight":"50px"}))
                        ]
                    )),
                    dbc.Col(dbc.Card(
                        [
 
                            dbc.CardBody(html.H1("test", style={"textAlign":"center", "color":"#0D1E2E"})),
                            dbc.CardFooter(html.P("test"))
                        ]
                    )),
                ]
            )
        ],
        style={"paddingTop":50,"color":"#0D1E2E"}
    )
)
 
random_graph_test = html.Div(
    dbc.Container(
        dcc.Graph(
            figure= {
                'data' : [
                        {'x': np.arange(np.datetime64('2019-11-01'), np.datetime64('2019-11-21')), 
                        'y': np.random.randint(0, 10, 20), 'type': 'line'}
                ],
                'layout' : {
                    'title': 'Random graph',
                    'xaxis': {'title':'Timeline'},
                    'yaxis': {'title':'Random', 'rangemode':"tozero"},
                    'font' : {'color':"#0D1E2E"}
                }
            },
        ),
        style={"paddingTop":50, "color":"#0D1E2E"}
    )
)


layout = html.Div(
    [
        row_header,
        kpis,
        random_graph_test
        
    ]
)





