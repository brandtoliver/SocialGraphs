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

degree_plot = pickle.load(open("data/binsN_all.p", "rb"))
n, bins = degree_plot
x = bins[:-1]+ 0.5*(bins[1:] - bins[:-1])
intro = html.Div(
        dbc.Row([
            dbc.Col(html.P("The page should say clearly what the dataset is and give the reader some idea of its most important properties "),className="pretty_container",width={'size':5, "order": 1}),
            dbc.Col([html.P("explain about data"),dbc.Button("Download Data", href='https://raw.githubusercontent.com/brandtoliver/SocialGraphs/master/df_all.csv', external_link=True, outline=True, color="secondary", className="mr-1")],className="pretty_container",width={'size':4, "order": 2}),
            dbc.Col([dbc.Row([html.Div([html.H5("Num of nodes:"),html.H3("482")])], style={"height": 135, "width":150, 'text-align': 'center'}, className="pretty_container", align="center"),
                    dbc.Row([html.Div([html.H5("Num of edges:"),html.H3("4173")])], style={"height": 135, "width":150, 'text-align': 'center'}, className="pretty_container", align="center"), #,html.Br()
                    dbc.Row([html.Div([html.H5("Avg. degree:"),html.H3("17.32")])], style={"height": 135, "width":150, 'text-align': 'center'}, className="pretty_container", align="center"),
                    dbc.Row([html.Div([html.H5("Num of questions:"),html.H3("49129")])], style={"height": 135, "width":150, 'text-align': 'center'}, className="pretty_container", align="center")], align='center', width={"order": 3})
            ],justify='center'))

##############
network_analysis_intro = html.Div(dbc.Row(dbc.Col([html.H2("Who is asking who?")],style={'text-align':'center'})),className='pretty_container')
##############

data_full_network = pickle.load(open("data/data_full_network.p", "rb"))
num_nodes = 474
fig = go.Figure(data=data_full_network,
             layout=go.Layout(
                plot_bgcolor = "#f9f9f9",
                paper_bgcolor= "#f9f9f9",
                height = 600,
                width = 600,
                #title='<br>Network Graph of '+str(num_nodes)+' rules',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=5,l=5,r=5,t=5),
                annotations=[ dict(
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

network1 = html.Div(
        dbc.Row([
            dbc.Col([html.P("Text about the network..."),
            dbc.ListGroup([
                dbc.ListGroupItem("Anders Fogh Rasmussen", href="/AndersFoghRasmussen", action=True),
                dbc.ListGroupItem("Lars Løkke I", href="/LarsLokkeI", action=True),
                dbc.ListGroupItem("Helle Thorning", href="/HelleThorning", action=True),
                dbc.ListGroupItem("Lars Løkke II", href="/LarsLokkeII", action=True),
                dbc.ListGroupItem("Mette Frederiksen", href="/MetteFrederiksen", action=True),
                ])], className="pretty_container", width = 3),
            dbc.Col(dcc.Graph(id='network_Graph',figure=fig), className="pretty_container", width = 'auto'),
            dbc.Col(dcc.Graph(id="degree_plot", style={'backgroundColor':'#f9f9f9'},
                figure={"data":[{'x':n, 'y':x, 'type':'scatter', 'marker':{'size': 10}}
             ], "layout": {"title":"Degree distribution","height":450, "width":350, "xaxis":{"title":"Degree (log)", "type":'log','showgrid':False}, "yaxis":{"title":"Frequency (log)","type":'log','showgrid':False}, "paper_bgcolor":"#f9f9f9", "plot_bgcolor":"#f9f9f9", 'margin': {'l': 10, 'b': 80, 't': 80, 'r': 5}}}), width = 3, className="pretty_container")
        ],justify='center')
    )


#############
df = pd.read_csv('data/question_time_data.csv')
dropdown = {'V': 'Venstre','S': 'Socialdemokratiet', 'ALT': 'Alternativet','EL': 'Enhedslisten','KF': 'Det Konservative Folkeparti','DF': 'Dansk Folkeparti','LA': 'Liberal Alliance','NB': 'Nye Borgerlige','RV': 'Radikale Venstre','SF': 'Socialistisk Folkeparti','UFG': 'Uden for folketingsgrupperne','udpeget af SF': 'udpeget af SF'}
Parti_farver = {'ALT':'#2b8738','DF':'#eac73e','EL':'#e6801a','KD':'#8b8474','KF':'#96b226','LA':'#3fb2be','NB':'#127b7f','RV':'#733280','S':'#a82721','SF':'#e07ea8','UFG':'#663300','V':'#254264', "minister":'#000000', 'udpeget af SF':'#e07ea8'}

question_time = html.Div(
    dbc.Row([
        dbc.Col(dcc.Graph(id="question_time_graph",style={'backgroundColor':'#f9f9f9'})),
        dbc.Col([html.P("First the number of $20-questions over time is visualised. From the figure on the left it is apparent that some members of parlament tend to only ask questions when not part of the government. Below you can select which of the parties to display in the graph."),
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
                                            multi=True, value=['V','S', 'DF'], style={"margin-left": "auto","margin-right": "auto","width": "100%"}) ], width='5')],className="pretty_container"))


@app.callback(Output('question_time_graph', 'figure'),
            [Input('question_time_dropdown', 'value')])
def update_question_time(selected_dropdown_value):
    trace = []
    for party in selected_dropdown_value:
        trace.append(go.Scatter(x=df['Date'], y=df[party], mode='lines', name=dropdown[party],
        marker=dict(color=Parti_farver[party])))

    figure = {'data': trace, 'layout': go.Layout(title="Number of §20-questions over time",
    xaxis={"title":"Date", 'showgrid':False},yaxis={"title":"Number of questions",'showgrid':False}, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', width=800, height =350)}
    return figure

##############
Text_analysis = html.Div(dbc.Row(dbc.Col([html.H2("What are the questions about?")],style={'text-align':'center'})), className='pretty_container')
##############

df_sentiment = pd.read_csv('data/sentiment1.csv')
x_data, y_data = ['Alternativet','Dansk Folkeparti','Enhedslisten','Det Konservative Folkeparti','Liberal Alliance','Nye Borgerlige','Radikale Venstre','Socialdemokratiet','Socialistisk Folkeparti','Uden for folketingsgrupperne','Venstre','udpeget af SF'], [-0.01436891, -0.18021013, -0.16699769 -0.06721895, -0.03019641, -0.00694444, -0.02127265, -0.07460463, -0.0760947, -0.03202512, -0.0478786 , -0.01990741]

Sentiment2 = html.Div([
    dbc.Row([
        dbc.Col([html.P(["Are some question more positive or negative than other? Do some parties ask mostly negative questions? Has the sentiment change over the years? A sentiment analysis is performed to anwser this, using a wordlist-based approach", html.A(' (AFINN sentiment analysis)',href='https://github.com/fnielsen/afinn'), html.P(" Words are scored from -5 (very negative) to +5 (very positive) and averaged pr. question.")]),dcc.Dropdown(id="sentiment2_dropdown", options=[{'label':'Venstre', 'value': 'V'},
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
                                        multi=True, value=['V','S', 'DF'], style={"margin-left": "auto","margin-right": "auto","width": "100%"})], className="pretty_container"),
        dbc.Col(dcc.Graph(id="sentiment2_graph",style={'backgroundColor':'#f9f9f9'}), style={"margin-left": "auto","margin-right": "auto","width": "100%"}, className="pretty_container"),
        dbc.Col(dcc.Graph(id="bar_plot", style={'backgroundColor':'#f9f9f9'},
            figure={"data":[{'x':y_data,'y':x_data, 'type':'bar', 'orientation':'h',
            "marker" : dict(color=['#2b8738','#eac73e','#e6801a','#96b226','#3fb2be','#127b7f','#733280','#a82721','#e07ea8','#663300','#254264','#e07ea8'],
            )}], "layout": {"title":"Avg. Sentiment of parties","height":350, "width":"400", "xaxis":{"title":"Avg. sentiment"}, "paper_bgcolor":"#f9f9f9", "plot_bgcolor":"#f9f9f9", 'margin': {'l': 180, 'b': 50, 't': 80, 'r': 50}}}), className="pretty_container", width='auto')
        ])
    ])

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
word_graph_data = pickle.load(open("data/dash_data.p", "rb"))
Parti_farver_hsl = {'ALT':[128,52,35],'DF':[48,80,58],'EL':[30,80,50],'KD':[42,9,50],'KF':[72,65,42],'LA':[186,50,50],'NB':[182,75,28],'RV':[290,44,35],'S':[3,67,39],'SF':[334,61,69],'UFG':[30,100,20],'V':[212,46,27], 'udpeget af SF':[334,61,69]}

word_cloud = html.Div(
    dbc.Row([
        dbc.Col([html.P("A wordcloud of 'important' words are displayed to the left. The importantness of words are determined by how many times a word is used by a party offset by how many times other parties use that word (TF-IDF). Select a party using the dropdown below."),
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
                                            multi=False, value='DF', style={"margin-left": "auto","margin-right": "auto","width": "100%", "margin-bottom": "15px"}),
                                            html.P("These words could be interpreted as the important topics of a given party. Looking at the top words across differnt parties it is clear that these words are indeed unique for each party. To investigate whether these words/topics are the result of a single big event causing many questions about this, or the parties thoughout there time in parlament keep asking about the same things, frequencies of top 5 words are visualised over time.") ], width=4),
        dbc.Col([html.Img(id='word_cloud')], width='auto'),
        dbc.Col(dcc.Graph(id="word_graph",style={'backgroundColor':'#f9f9f9'}))
    ],className="pretty_container")
)

def plot_wordcloud(data, party):
    wc = WordCloud(background_color='#f9f9f9', width=410, height=390)
    wc.generate_from_frequencies(frequencies=data)

    def party_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        h, s, l = Parti_farver_hsl[party]
        return "hsl(" + str(h) + "," + str(s) + "%," + str(random.randint(l-15, l)) + "%)"

    wc.recolor(color_func=party_color_func, random_state=3)
    return wc.to_image()

@app.callback([dd.Output('word_cloud', 'src'),
                dd.Output('word_graph', 'figure')],
            [dd.Input('word_cloud_dropdown', 'value')])
def make_image_and_graph(party):
    trace = []
    data = word_graph_data[party]

    # Move to notebook
    data['Date'] = data.index
    data['Date'] = data['Date'].apply(np.datetime64)

    for word in data.columns[:5]:
        trace.append(go.Scatter(x=data['Date'], y=data[word], mode='lines', name=word
        ))

    figure = {'data': trace, 'layout': go.Layout(title="Top 5 words over time",
    xaxis={'showgrid':False},yaxis={"title":"Frequency",'showgrid':False}, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', width=460,height= 400, legend_orientation="h", margin={'l': 70, 'b': 60, 't': 60, 'r': 0})}

    img = BytesIO()
    plot_wordcloud(data=word_cloud_data[party], party=party).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode()), figure

word_cloud_pos_neg = html.Div(dbc.Row([
                                dbc.Col([
                                    html.P("Having analysed the sentiment, it makes sense to also look at what words are being used when the questions are considerably negative or positive. Negative or positive are defined as questions with average sentiment lower or higher than 2 standard deviations from the mean."),
                                    dcc.Dropdown(id="word_cloud_dropdown_2", options=[{'label':'Venstre', 'value': 'V'},
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
                                                                    multi=False, value='SF', style={"margin-left": "auto","margin-right": "auto","width": "100%", "margin-bottom": "15px"}),
                                                                    html.P("Text.fjdfgjkhfgkhjdfgkjhdfgjhkdfjhkdjhkgfdfgjhkdfgkjhdfjkh")], width=4),
                                dbc.Col([html.H3("Positive"),html.Img(id='word_cloud_pos')],style={'text-align':'center'}, width=4),
                                dbc.Col([html.H3("Negative"),html.Img(id='word_cloud_neg')],style={'text-align':'center'}, width=4),
                                ]
                            ),className="pretty_container")

data_pos_neg = pickle.load(open("data/wordcloud_pos_neg.p", "rb"))

@app.callback([dd.Output('word_cloud_pos', 'src'),
                dd.Output('word_cloud_neg', 'src')],
            [dd.Input('word_cloud_dropdown_2', 'value')])
def make_wordcloud(party1):
    img_pos, img_neg = BytesIO(), BytesIO()
    data_pos, data_neg = data_pos_neg
    plot_wordcloud(data=data_pos[party1], party=party1).save(img_pos, format='PNG')
    plot_wordcloud(data=data_neg[party1], party=party1).save(img_neg, format='PNG')

    return 'data:image/png;base64,{}'.format(base64.b64encode(img_pos.getvalue()).decode()), 'data:image/png;base64,{}'.format(base64.b64encode(img_neg.getvalue()).decode())

layout = html.Div(
    [
        intro,
        network_analysis_intro,
        network1,
        question_time,
        Text_analysis,
        #Sentiment1,
        word_cloud,
        Sentiment2,
        word_cloud_pos_neg
    ]
)
#threaded=True
