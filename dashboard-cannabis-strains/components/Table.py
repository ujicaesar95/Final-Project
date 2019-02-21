import dash_html_components as html
import dash_table as dt
import pandas as pd
import numpy as np

PAGE_SIZE = 10

strains = pd.read_csv('strains_data.csv')

def generate_table(dataframe) :
    return dt.DataTable(
        id='table-multicol-sorting',
        columns=[
            {"name": i, "id": i} for i in dataframe.columns
        ],
        pagination_settings={
            'current_page': 0,
            'page_size': PAGE_SIZE
        },
        pagination_mode='be',

        sorting='be',
        sorting_type='multi',
        sorting_settings=[],
        style_table={'overflowX': 'scroll'}
    )

def renderTable(df) :
    return html.Div([
                html.H1('Data Strains Cannabis', className='h1'),
                generate_table(df)
            ])