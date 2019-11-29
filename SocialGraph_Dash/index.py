import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd 
import numpy as np

from app import app
from apps import text, network, home


#Top navbar
navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(
                        
                        html.H4("Social graphs and interactions", style={"fontSize":50, "fontFamily":"Georgia"}),style={"color":"white","textAlign":"center","paddingTop":10}  
                        
                    ),         
                ],
        
                align="center",
                no_gutters=True,
                
            ),
            
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        #dbc.Collapse(right_bar, id="navbar-collapse", navbar=True),     
    ],
    dark = True,
    #className="test"  
    #color="dark", 
)



#Left side navbar
vertical_navbar = dbc.Col(
    [
        dbc.Nav(
            [
                dbc.Card(
                    
                    dbc.Button(
                        "Overview",
                        style={"backgroundColor":"#0D1E2E", "borderColor":"#0D1E2E", "color":"#f2f2f2", "fontFamily": "Georgia", "fontSize":25},  
                        outline=False,
                        #color="dark",
                        href="/overview"
                        
                    )
                ),    
                dbc.Card(
                    [
                        dbc.Button(
                            "Administrations",
                            id="pur-toggle",
                            style={"backgroundColor":"#0D1E2E", "borderColor":"#0D1E2E", "color":"#f2f2f2", "fontFamily": "Georgia", "fontSize":25},  
                            outline=False,
                            href="/Administration"
                        ), 
                        dbc.Collapse(
                            dbc.CardBody(
                                dbc.Nav(
                                    [
                                        dbc.Button(
                                        "Administration 1",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f", "fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration1"
                                        ),
                                        dbc.Button(
                                        "Administration 2",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration2"
                                        ),
                                         dbc.Button(
                                        "Administration 3",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration3"
                                        ),
                                         dbc.Button(
                                        "Administration 4",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration4"
                                        ),
                                         dbc.Button(
                                        "Administration 5",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration5"
                                        ),
                                         dbc.Button(
                                        "Administration 6",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration6"
                                        ),
                                         dbc.Button(
                                        "Administration 7",
                                        style={"backgroundColor":"#0D1E2E", "color":"white","borderColor":"#132a3f","fontFamily": "Georgia", "fontSize":20},  
                                        outline=False,
                                        href="/Administration7"
                                        ),
                                       
                                    ],
                                    vertical=True,
                                )
                            ),
                            id="collapse-pur",
                        ),
                    ], className="collapse_button",
                    style={"backgroundColor":"#d6dbda"}
                ),

                dbc.Card(
                    dbc.Button(
                        "Explainer notebook",
                        style={"backgroundColor":"#0D1E2E", "borderColor":"#0D1E2E", "color":"#f2f2f2", "fontFamily": "Georgia", "fontSize":25},  
                        outline=False,
                        href="Explainer"
                    ),
                )
            ],
            vertical=True,
        ),
    ],
    width=2,
    className="leftbar light",
    style={"backgroundColor":"#0D1E2E", "height":"1000px"}
)


#app layout: 


app.layout = html.Div(
    [   
        dcc.Location(id = 'url', refresh = False),
        navbar,
        dbc.Row(
            [
                vertical_navbar,
                html.Div(id='page-content')
            ], 
            no_gutters=True,
            

        )
    ], 
    className="overlay"
)


#App callback - Tells us where a button takes us:
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/overview':
        return network.layout
    elif pathname == '/text':
        return text.layout
    else:
        return home.layout


@app.callback(
    Output(f"collapse-pur", "is_open"),
    [Input(f"pur-toggle", "n_clicks")],
    [State(f"collapse-pur", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__=='__main__':
    app.run_server(debug=True)
