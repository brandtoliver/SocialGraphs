import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd 
import numpy as np

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.config.suppress_callback_exceptions = True
server = app.server

