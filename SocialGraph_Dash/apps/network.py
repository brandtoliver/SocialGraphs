import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as dd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from app import app

import numpy as np
from io import BytesIO
from wordcloud import WordCloud
import base64
import pandas as pd
import pickle
import random

intro = html.Div(
        dbc.Row([
            dbc.Col(html.P("This website aims to investigate the §20-questions from the danish parlament, the data is gathered from the website ... jksdhfjk kjweh rjkhsdfk hs dlkjh")),
            dbc.Col(html.P("This website aims to investigate the §20-questions from the danish parlament, the data is gathered from the website ... jksdhfjk kjweh rjkhsdfk hs dlkjh"))
            ]), className="pretty_container")

df = pd.read_csv('data/question_time_data.csv')
dropdown = {'V': 'Venstre','S': 'Socialdemokratiet', 'ALT': 'Alternativet','EL': 'Enhedslisten','KF': 'Det Konservative Folkeparti','DF': 'Dansk Folkeparti','LA': 'Liberal Alliance','NB': 'Nye Borgerlige','RV': 'Radikale Venstre','SF': 'Socialistisk Folkeparti','UFG': 'Uden for folketingsgrupperne','udpeget af SF': 'udpeget af SF'}
Parti_farver = {'ALT':'#2b8738','DF':'#eac73e','EL':'#e6801a','KD':'#8b8474','KF':'#96b226','LA':'#3fb2be','NB':'#127b7f','RV':'#733280','S':'#a82721','SF':'#e07ea8','UFG':'#663300','V':'#254264', "minister":'#000000', 'udpeget af SF':'#e07ea8'}

question_time = html.Div(
    dbc.Row([
        dbc.Col(dbc.Container(dcc.Graph(id="question_time_graph",style={'backgroundColor':'#f9f9f9'})), className="pretty_container"),
        dbc.Col([html.P("First the number of $20-questions over time is visualised. From the figure on the left it is apparent that memebers of parlament tend to only ask questions when not part of the government. Below you can select which of the parties to display in the graph."),
        dcc.Dropdown(id="question_time_dropdown", options=[{'label':'Venstre', 'value': 'V'},
                                            {'label':'Socialdemokratiet', 'value': 'S'},
                                            {'label':'Alternativet', 'value': 'ALT'},
                                            {'label':'Enhedslisten', 'value': 'EL'},
                                            #{'label':'Kristendemokraterne', 'value': 'KD'},
                                            {'label':'Dansk Folkeparti', 'value': 'DF'},
                                            {'label':'Liberal Alliance', 'value': 'LA'},
                                            {'label':'Nye Borgerlige', 'value': 'NB'},
                                            {'label':'Radikale Venstre', 'value': 'RV'},
                                            {'label':'Socialistisk Folkeparti', 'value': 'SF'},
                                            {'label':'Uden for folketingsgrupperne', 'value': 'UFG'},
                                            {'label':'Det Konservative Folkeparti', 'value': 'KF'},
                                            {'label':'udpeget af SF', 'value': 'udpeget af SF'}],
                                            multi=True, value=['V','S', 'DF'], style={"margin-left": "auto","margin-right": "auto","width": "100%"}) ], className="pretty_container", width=3)]))


@app.callback(Output('question_time_graph', 'figure'),
            [Input('question_time_dropdown', 'value')])
def update_question_time(selected_dropdown_value):
    trace = []
    for party in selected_dropdown_value:
        trace.append(go.Scatter(x=df['Date'], y=df[party], mode='lines', name=dropdown[party],
        marker=dict(color=Parti_farver[party])))

    figure = {'data': trace, 'layout': go.Layout(title="Number of §20-questions over time",
    xaxis={"title":"Date", 'showgrid':False},yaxis={"title":"Number of questions",'showgrid':False}, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', width=700, height =300)}
    return figure

##############

df_sentiment = pd.read_csv('data/sentiment1.csv')

Sentiment1 = html.Div(
    dbc.Row([
        dbc.Col(dbc.Container(dcc.Graph(id="sentiment1_graph",style={'backgroundColor':'#f9f9f9'})), className="pretty_container"),
        dbc.Col([html.P("First the number of $20-questions over time is visualised. From the figure on the left it is apparent that memebers of parlament tend to only ask questions when not part of the government. Below you can select which of the parties to display in the graph."),
        dcc.Dropdown(id="sentiment1_dropdown", options=[{'label':'Venstre', 'value': 'V'},
                                            {'label':'Socialdemokratiet', 'value': 'S'},
                                            {'label':'Alternativet', 'value': 'ALT'},
                                            {'label':'Enhedslisten', 'value': 'EL'},
                                            #{'label':'Kristendemokraterne', 'value': 'KD'},
                                            {'label':'Dansk Folkeparti', 'value': 'DF'},
                                            {'label':'Liberal Alliance', 'value': 'LA'},
                                            {'label':'Nye Borgerlige', 'value': 'NB'},
                                            {'label':'Radikale Venstre', 'value': 'RV'},
                                            {'label':'Socialistisk Folkeparti', 'value': 'SF'},
                                            {'label':'Uden for folketingsgrupperne', 'value': 'UFG'},
                                            {'label':'Det Konservative Folkeparti', 'value': 'KF'},
                                            {'label':'udpeget af SF', 'value': 'udpeget af SF'}],
                                            multi=True, value=['V','S', 'DF'], style={"margin-left": "auto","margin-right": "auto","width": "100%"}) ], className="pretty_container", width=3)
    ])
)
@app.callback(Output('sentiment1_graph', 'figure'),
            [Input('sentiment1_dropdown', 'value')])
def update_sentiment1(selected_dropdown_value):
    trace = []
    for party in selected_dropdown_value:
        trace.append(go.Histogram(x=df_sentiment[df_sentiment.Parti == party], name=dropdown[party], opacity=0.3, marker={"line": {"color": Parti_farver[party]}}, histnorm='probability'))
    layout = go.Layout(title=f"Age Distribution", xaxis={"title": "Age (years)", "showgrid": False},
                       yaxis={"title": "Count", "showgrid": False}, )
    figure2 = {"data": trace, "layout": layout}
    return figure2

#################

df_sentiment = pd.read_csv('data/sentiment1.csv')

Sentiment2 = html.Div(
    dbc.Row([
        dbc.Col(dbc.Container(dcc.Graph(id="sentiment2_graph",style={'backgroundColor':'#f9f9f9'})), className="pretty_container"),
        dbc.Col([html.P("First the number of $20-questions over time is visualised. From the figure on the left it is apparent that memebers of parlament tend to only ask questions when not part of the government. Below you can select which of the parties to display in the graph."),
        dcc.Dropdown(id="sentiment2_dropdown", options=[{'label':'Venstre', 'value': 'V'},
                                            {'label':'Socialdemokratiet', 'value': 'S'},
                                            {'label':'Alternativet', 'value': 'ALT'},
                                            {'label':'Enhedslisten', 'value': 'EL'},
                                            #{'label':'Kristendemokraterne', 'value': 'KD'},
                                            {'label':'Dansk Folkeparti', 'value': 'DF'},
                                            {'label':'Liberal Alliance', 'value': 'LA'},
                                            {'label':'Nye Borgerlige', 'value': 'NB'},
                                            {'label':'Radikale Venstre', 'value': 'RV'},
                                            {'label':'Socialistisk Folkeparti', 'value': 'SF'},
                                            {'label':'Uden for folketingsgrupperne', 'value': 'UFG'},
                                            {'label':'Det Konservative Folkeparti', 'value': 'KF'},
                                            {'label':'udpeget af SF', 'value': 'udpeget af SF'}],
                                            multi=True, value=['V','S', 'DF'], style={"margin-left": "auto","margin-right": "auto","width": "100%"}) ], className="pretty_container", width=3)
    ])
)
@app.callback(Output('sentiment2_graph', 'figure'),
            [Input('sentiment2_dropdown', 'value')])
def update_sentiment2(selected_dropdown_value):
    trace = []
    for party in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sentiment['Date'], y=df_sentiment[party], mode='lines', name=dropdown[party],
        marker=dict(color=Parti_farver[party])))

    figure = {'data': trace, 'layout': go.Layout(title="Sentiment of §20-questions over time",
    xaxis={"title":"Date", 'showgrid':False},yaxis={"title":"Average sentiment",'showgrid':False}, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', width=700,height =400)}
    return figure

#################

word_cloud_data = pickle.load(open("data/wordcloud.p", "rb"))

Parti_farver_hsl = {'ALT':[128,52,35],'DF':[48,80,58],'EL':[30,80,50],'KD':[42,9,50],'KF':[72,65,42],'LA':[186,50,50],'NB':[182,75,28],'RV':[290,44,35],'S':[3,67,39],'SF':[334,61,69],'UFG':[30,100,20],'V':[212,46,27], 'udpeget af SF':[334,61,69]}

word_cloud = html.Div(
    dbc.Row([
        dbc.Col([html.P("First the number of $20-questions over time is visualised. From the figure on the left it is apparent that memebers of parlament tend to only ask questions when not part of the government. Below you can select which of the parties to display in the graph."),
        dcc.Dropdown(id="word_cloud_dropdown", options=[{'label':'Venstre', 'value': 'V'},
                                            {'label':'Socialdemokratiet', 'value': 'S'},
                                            {'label':'Alternativet', 'value': 'ALT'},
                                            {'label':'Enhedslisten', 'value': 'EL'},
                                            #{'label':'Kristendemokraterne', 'value': 'KD'},
                                            {'label':'Dansk Folkeparti', 'value': 'DF'},
                                            {'label':'Liberal Alliance', 'value': 'LA'},
                                            {'label':'Nye Borgerlige', 'value': 'NB'},
                                            {'label':'Radikale Venstre', 'value': 'RV'},
                                            {'label':'Socialistisk Folkeparti', 'value': 'SF'},
                                            {'label':'Uden for folketingsgrupperne', 'value': 'UFG'},
                                            {'label':'Det Konservative Folkeparti', 'value': 'KF'},
                                            {'label':'udpeget af SF', 'value': 'udpeget af SF'}],
                                            multi=False, value='DF', style={"margin-left": "auto","margin-right": "auto","width": "100%"}) ], className="pretty_container", width=3),
        dbc.Col(html.Img(id='word_cloud'), className="pretty_container")
    ])
)


    #return "hsl(48, 80%, 58%)"

def plot_wordcloud(data, party):
    #d = {a: x for a, x in data.values}
    #data = dict(word_cloud_data[1].items())
    data = word_cloud_data[party]
    wc = WordCloud(background_color='#f9f9f9', width=480, height=360)
    wc.generate_from_frequencies(frequencies=data)

    def party_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        #x = 58
        h, s, l = Parti_farver_hsl[party]
        return "hsl(" + str(h) + "," + str(s) + "%," + str(random.randint(l-15, l)) + "%)"

    wc.recolor(color_func=party_color_func, random_state=3)
    #wc.fit_words(d)
    return wc.to_image()

@app.callback(dd.Output('word_cloud', 'src'),
            [dd.Input('word_cloud_dropdown', 'value')])
def make_image(party):
    img = BytesIO()
    plot_wordcloud(data=word_cloud_data, party=party).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

layout = html.Div(
    [
        intro,
        question_time,
        #Sentiment1,
        word_cloud,
        Sentiment2

    ]
)
