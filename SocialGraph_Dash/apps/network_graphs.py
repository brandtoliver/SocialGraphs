from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
from fa2 import ForceAtlas2
import re as re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
from unidecode import unidecode
import urllib
import json
import urllib.request
import pickle
from tqdm import tqdm_notebook
import re
from fa2 import ForceAtlas2
from itertools import islice
import os
import community
import seaborn as sns
import matplotlib as mpl
from operator import itemgetter
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import warnings
#warnings.filterwarnings("ignore")
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import networkx as nx

from app import app



data_full_network = pickle.load(open("data/data_full_network.p", "rb"))

num_nodes = 474

fig = go.Figure(data=data_full_network,
             layout=go.Layout(
                plot_bgcolor = "#f9f9f9", 
                height= 900,
                title='<br>Network Graph of '+str(num_nodes)+' rules',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                #margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

full_Network = html.Div(

    dbc.Row(dbc.Col(dcc.Graph(id='Graph',figure=fig)),className="pretty_container")

    
)

"""
full_Network = html.Div([
                html.Div(dcc.Graph(id='Graph',figure=fig)),
                html.Div(className='row', children=[
                    html.Div([html.H2('Overall Data'),
                              html.P('Num of nodes: ' + str("474")),
                              html.P('Num of edges: ' + str("474"))],
                              className='pretty container'),
                    html.Div([
                            html.H2('Selected Data'),
                            html.Div(id='selected-data'),
                        ], className='six columns')
                    ])
                ])

"""

@app.callback(
    Output('selected-data', 'children'),
    [Input('Graph','selectedData')])
def display_selected_data(selectedData):
    num_of_nodes = len(selectedData['points'])
    text = [html.P('Num of nodes selected: '+str(num_of_nodes))]
    for x in selectedData['points']:
#        print(x['text'])
        split1, split2 =x['text'].split("<br>") 
        material = split1  
        material2 = split2
    
        #material = x['text'].split('<br>')[0][7:]
    
        text.append(html.P(str(material)+", "+str(material2)))
    return text



layout = html.Div(
    [
      full_Network

    ]

)