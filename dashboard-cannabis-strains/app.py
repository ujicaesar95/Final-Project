import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pickle
from components.Table import renderTable
from components.scatterPlot import renderScatterPlot
from components.modelPredict import renderModelPredict
from components.updateDict import updateDict



# loadModel = pickle.load(open('rfc_model.sav', 'rb'))
loadModel = pickle.load(open('gbc_strains.sav', 'rb'))
app = dash.Dash(__name__)

server = app.server

strains = pd.read_csv('strains_deploy.csv')

app.title = 'Dashboard Strains Cannabis'

app.layout = html.Div(children=[
    html.H1(children='Dashboard Strains Cannabis (by Fauzy Caesarrochim))',className='titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Table Strains Dataset', value='tab-1',children=[
            renderTable(strains)
        ]),
        dcc.Tab(label='Type Distribution Scatter Plot', value='tab-2',children=[
            renderScatterPlot(strains)
        ]),
        dcc.Tab(label='Test Predict', value='tab-3',children=[
            renderModelPredict()
        ]),
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])

def update_graph(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = strains.head(500).sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = strains.head(500)

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputPrice', 'value'), 
    State('inputRating', 'value'),
    State('inputEffects1', 'value'),
    State('inputEffects2', 'value'),
    State('inputEffects3', 'value'),
    State('inputEffects4', 'value'),
    State('inputEffects5', 'value'),
    State('inputFlavor1', 'value'),
    State('inputFlavor2', 'value'),
    State('inputFlavor3', 'value')
      ])

def update_output (n_clicks, Price, Rating ,Effects1,Effects2,Effects3,Effects4,Effects5,Flavor1,Flavor2,Flavor3) :
    
    dictio = updateDict(Effects1,Effects2,Effects3,Effects4,Effects5,Flavor1,Flavor2,Flavor3)

    data = [Rating, Price]

    for i in dictio.values():
        data.append(i)
    # print(len(data))
    data = np.array([data])
    print(data)
    # data = pd.DataFrame(data).T

    prediction = loadModel.predict(data)
    predictProba = loadModel.predict_proba(data)
    hasil = ''
    print(prediction)
    print(predictProba)
    if(prediction[0] == 1) :
        hasil = 'Sativa'
        predik = predictProba[0][1]
    elif(prediction[0] == 2):
        hasil = 'Indica'
        predik = predictProba[0][2]
    else:
        hasil = 'Hybrid'
        predik = predictProba[0][0]

    return ('Prediction : ' + hasil + " | Predict Proba : " + str(predik) )



if __name__ == '__main__':
    app.run_server(debug=True,port=2019)