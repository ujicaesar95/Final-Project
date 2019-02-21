import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

color_set = ['#80aaff','#cc0000']

def legend(val) :
    if(val == 2) :
        return 'indica'
    elif(val == 1) :
        return 'sativa'
    else :
        return 'hybrid'

def renderScatterPlot(df) :
    return html.Div([
                html.H1('Scatter Plot Strains Cannabis', className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df[df['Type'] == col].head(500)['Rating'],
                                y=df[df['Type'] == col].head(500)['Price'],
                                mode='markers',
                                # marker=dict(color=color_set[i], size=10, line=dict(width=0.5, color='white')),
                                name=legend(col)
                            ) for col in df['Type'].unique()
                        ],
                        'layout': go.Layout(
                            xaxis= dict(title='Type'),
                            yaxis={'title': 'Price'},
                            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                            hovermode='closest'
                        )
                    }
                )
            ])