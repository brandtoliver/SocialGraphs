import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np

from app import app
from apps import text, network, home, MF

navbar1 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Overview", href="overview")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Individual administrations", header=True),
                dbc.DropdownMenuItem("Anders Fogh Rasmussen", href="AndersFoghRasmussen"),
                dbc.DropdownMenuItem("Lars Løkke I", href="LarsLokkeI"),
                dbc.DropdownMenuItem("Helle Thorning", href="HelleThorning"),
                dbc.DropdownMenuItem("Lars Løkke II", href="LarsLokkeII"),
                dbc.DropdownMenuItem("Mette Frederiksen", href="MetteFrederiksen")
            ],
            nav=True,
            in_navbar=True,
            label="Administrations",
        ),
        dbc.NavItem(dbc.NavLink("Explainer notebook", href="https://github.com/brandtoliver/SocialGraphs")),
    ],
    brand="Parliamentary §20-Questions",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div(
    [
        dcc.Location(id = 'url', refresh = False),
        navbar1,
        dbc.Row(
            [
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

    elif pathname == '/MetteFrederiksen':
        return MF.layout
    elif pathname == '/LarsLokkeII':
        return text.layout
    elif pathname == '/HelleThorning':
        return text.layout
    elif pathname == '/LarsLokkeI':
        return text.layout
    elif pathname == '/AndersFoghRasmussen':
        return text.layout
    else:
        return network.layout


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

#app.config.suppress_callback_exceptions = True

if __name__=='__main__':
    app.run_server(debug=True)
