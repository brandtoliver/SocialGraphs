import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd 
import numpy as np

#from apps.funcs import *

row_header = html.Div(
    [
        dbc.Row(dbc.Col(html.H1("This is the content of homepage"),style={"color":"#0D1E2E","textAlign":"center","paddingTop":30})),  
    ]
)



layout = html.Div(
    [
        row_header
    
        
    ]
)

