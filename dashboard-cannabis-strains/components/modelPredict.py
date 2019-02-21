import dash_core_components as dcc
import dash_html_components as html

def renderModelPredict() :
    return html.Div([
                html.H1('Test Predict Strains Cannabis', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Price : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputPrice', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Rating : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputRating', options=[
                            {'label' : '3.', 'value' : 3.0},
                            {'label' : '3.1', 'value' : 3.1},
                            {'label' : '3.2', 'value' : 3.2},
                            {'label' : '3.3', 'value' : 3.3},
                            {'label' : '3.4', 'value' : 3.4},
                            {'label' : '3.5', 'value' : 3.5},
                            {'label' : '3.6', 'value' : 3.6},
                            {'label' : '3.7', 'value' : 3.7},
                            {'label' : '3.8', 'value' : 3.8},
                            {'label' : '3.9', 'value' : 3.9},
                            {'label' : '4.', 'value' : 4.0},
                            {'label' : '4.1', 'value' : 4.1},
                            {'label' : '4.2', 'value' : 4.2},
                            {'label' : '4.3', 'value' : 4.3},
                            {'label' : '4.4', 'value' : 4.4},
                            {'label' : '4.5', 'value' : 4.5},
                            {'label' : '4.6', 'value' : 4.6},
                            {'label' : '4.7', 'value' : 4.7},
                            {'label' : '4.8', 'value' : 4.8},
                            {'label' : '4.9', 'value' : 4.9},
                            {'label' : '5.', 'value' : 5.0}
                        ], value='3.')
                    ],className='col-4'),
                    html.Div([
                        html.P('Effects1 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputEffects1', options=[
                            {'label' : 'Aroused', 'value' : 'Aroused'},
                            {'label' : 'Creative', 'value' : 'Creative'},
                            {'label' : 'Dry', 'value' : 'Dry'},
                            {'label' : 'Energetic', 'value' : 'Energetic'},
                            {'label' : 'Euphoric', 'value' : 'Euphoric'},
                            {'label' : 'Focused', 'value' : 'Focused'},
                            {'label' : 'Giggly', 'value' : 'Giggly'},
                            {'label' : 'Happy', 'value' : 'Happy'},
                            {'label' : 'Hungry', 'value' : 'Hungry'},
                            {'label' : 'None', 'value' : 'None'},
                            {'label' : 'Relaxed', 'value' : 'Relaxed'},
                            {'label' : 'Sleepy', 'value' : 'Sleepy'},
                            {'label' : 'Talkative', 'value' : 'Talkative'},
                            {'label' : 'Tingly', 'value' : 'Tingly'},
                            {'label' : 'Uplifted', 'value' : 'Uplifted'}  
                        ], value='None' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Effects2 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputEffects2', options=[
                            {'label' : 'Aroused', 'value' : 'Aroused'},
                            {'label' : 'Creative', 'value' : 'Creative'},
                            {'label' : 'Dry', 'value' : 'Dry'},
                            {'label' : 'Energetic', 'value' : 'Energetic'},
                            {'label' : 'Euphoric', 'value' : 'Euphoric'},
                            {'label' : 'Focused', 'value' : 'Focused'},
                            {'label' : 'Giggly', 'value' : 'Giggly'},
                            {'label' : 'Happy', 'value' : 'Happy'},
                            {'label' : 'Hungry', 'value' : 'Hungry'},
                            {'label' : 'None', 'value' : 'None'},
                            {'label' : 'Relaxed', 'value' : 'Relaxed'},
                            {'label' : 'Sleepy', 'value' : 'Sleepy'},
                            {'label' : 'Talkative', 'value' : 'Talkative'},
                            {'label' : 'Tingly', 'value' : 'Tingly'},
                            {'label' : 'Uplifted', 'value' : 'Uplifted'}
                        ], value='None' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Effects3 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputEffects3', options=[
                            {'label' : 'Aroused', 'value' : 'Aroused'},
                            {'label' : 'Creative', 'value' : 'Creative'},
                            {'label' : 'Dry', 'value' : 'Dry'},
                            {'label' : 'Energetic', 'value' : 'Energetic'},
                            {'label' : 'Euphoric', 'value' : 'Euphoric'},
                            {'label' : 'Focused', 'value' : 'Focused'},
                            {'label' : 'Giggly', 'value' : 'Giggly'},
                            {'label' : 'Happy', 'value' : 'Happy'},
                            {'label' : 'Hungry', 'value' : 'Hungry'},
                            {'label' : 'None', 'value' : 'None'},
                            {'label' : 'Relaxed', 'value' : 'Relaxed'},
                            {'label' : 'Sleepy', 'value' : 'Sleepy'},
                            {'label' : 'Talkative', 'value' : 'Talkative'},
                            {'label' : 'Tingly', 'value' : 'Tingly'},
                            {'label' : 'Uplifted', 'value' : 'Uplifted'}
                        ], value='None' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Effects4 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputEffects4', options=[
                            {'label' : 'Aroused', 'value' : 'Aroused'},
                            {'label' : 'Creative', 'value' : 'Creative'},
                            {'label' : 'Dry', 'value' : 'Dry'},
                            {'label' : 'Energetic', 'value' : 'Energetic'},
                            {'label' : 'Euphoric', 'value' : 'Euphoric'},
                            {'label' : 'Focused', 'value' : 'Focused'},
                            {'label' : 'Giggly', 'value' : 'Giggly'},
                            {'label' : 'Happy', 'value' : 'Happy'},
                            {'label' : 'Hungry', 'value' : 'Hungry'},
                            {'label' : 'None', 'value' : 'None'},
                            {'label' : 'Relaxed', 'value' : 'Relaxed'},
                            {'label' : 'Sleepy', 'value' : 'Sleepy'},
                            {'label' : 'Talkative', 'value' : 'Talkative'},
                            {'label' : 'Tingly', 'value' : 'Tingly'},
                            {'label' : 'Uplifted', 'value' : 'Uplifted'}
                        ], value='None' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Effects5 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputEffects5', options=[
                            {'label' : 'Aroused', 'value' : 'Aroused'},
                            {'label' : 'Creative', 'value' : 'Creative'},
                            {'label' : 'Dry', 'value' : 'Dry'},
                            {'label' : 'Energetic', 'value' : 'Energetic'},
                            {'label' : 'Euphoric', 'value' : 'Euphoric'},
                            {'label' : 'Focused', 'value' : 'Focused'},
                            {'label' : 'Giggly', 'value' : 'Giggly'},
                            {'label' : 'Happy', 'value' : 'Happy'},
                            {'label' : 'Hungry', 'value' : 'Hungry'},
                            {'label' : 'None', 'value' : 'None'},
                            {'label' : 'Relaxed', 'value' : 'Relaxed'},
                            {'label' : 'Sleepy', 'value' : 'Sleepy'},
                            {'label' : 'Talkative', 'value' : 'Talkative'},
                            {'label' : 'Tingly', 'value' : 'Tingly'},
                            {'label' : 'Uplifted', 'value' : 'Uplifted'}
                        ], value='None' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Flavor1 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputFlavor1', options=[
                            {'label' : 'Ammonia', 'value' : 'Ammonia'},
                            {'label' : 'Apple', 'value' : 'Apple'},
                            {'label' : 'Apricot', 'value' : 'Apricot'},
                            {'label' : 'Berry', 'value' : 'Berry'},
                            {'label' : 'Blue', 'value' : 'Blue'},
                            {'label' : 'Blueberry', 'value' : 'Blueberry'},
                            {'label' : 'Butter', 'value' : 'Butter'},
                            {'label' : 'Cheese', 'value' : 'Cheese'},
                            {'label' : 'Chemical', 'value' : 'Chemical'},
                            {'label' : 'Chestnut', 'value' : 'Chestnut'},
                            {'label' : 'Citrus', 'value' : 'Citrus'},
                            {'label' : 'Coffee', 'value' : 'Coffee'},
                            {'label' : 'Diesel', 'value' : 'Diesel'},
                            {'label' : 'Earthy', 'value' : 'Earthy'},
                            {'label' : 'Flowery', 'value' : 'Flowery'},
                            {'label' : 'Fruit', 'value' : 'Fruit'},
                            {'label' : 'Grape', 'value' : 'Grape'},
                            {'label' : 'Grapefruit', 'value' : 'Grapefruit'},
                            {'label' : 'Honey', 'value' : 'Honey'},
                            {'label' : 'Lavender', 'value' : 'Lavender'},
                            {'label' : 'Lemon', 'value' : 'Lemon'},
                            {'label' : 'Lime', 'value' : 'Lime'},
                            {'label' : 'Mango', 'value' : 'Mango'},
                            {'label' : 'Menthol', 'value' : 'Menthol'},
                            {'label' : 'Mint', 'value' : 'Mint'},
                            {'label' : 'Minty', 'value' : 'Minty'},
                            {'label' : 'None.1', 'value' : 'None.1'},
                            {'label' : 'Nutty', 'value' : 'Nutty'},
                            {'label' : 'Orange', 'value' : 'Orange'},
                            {'label' : 'Peach', 'value' : 'Peach'},
                            {'label' : 'Pear', 'value' : 'Pear'},
                            {'label' : 'Pepper', 'value' : 'Pepper'},
                            {'label' : 'Pine', 'value' : 'Pine'},
                            {'label' : 'Pineapple', 'value' : 'Pineapple'},
                            {'label' : 'Pungent', 'value' : 'Pungent'},
                            {'label' : 'Rose', 'value' : 'Rose'},
                            {'label' : 'Sage', 'value' : 'Sage'},
                            {'label' : 'Skunk', 'value' : 'Skunk'},
                            {'label' : 'Spicy/Herbal', 'value' : 'Spicy/Herbal'},
                            {'label' : 'Strawberry', 'value' : 'Strawberry'},
                            {'label' : 'Sweet', 'value' : 'Sweet'},
                            {'label' : 'Tar', 'value' : 'Tar'},
                            {'label' : 'Tea', 'value' : 'Tea'},
                            {'label' : 'Tobacco', 'value' : 'Tobacco'},
                            {'label' : 'Tree', 'value' : 'Tree'},
                            {'label' : 'Tropical', 'value' : 'Tropical'},
                            {'label' : 'Vanilla', 'value' : 'Vanilla'},
                            {'label' : 'Violet', 'value' : 'Violet'},
                            {'label' : 'Woody', 'value' : 'Woody'}
                        ], value='None.1' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Flavor2 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputFlavor2', options=[
                            {'label' : 'Ammonia', 'value' : 'Ammonia'},
                            {'label' : 'Apple', 'value' : 'Apple'},
                            {'label' : 'Apricot', 'value' : 'Apricot'},
                            {'label' : 'Berry', 'value' : 'Berry'},
                            {'label' : 'Blue', 'value' : 'Blue'},
                            {'label' : 'Blueberry', 'value' : 'Blueberry'},
                            {'label' : 'Butter', 'value' : 'Butter'},
                            {'label' : 'Cheese', 'value' : 'Cheese'},
                            {'label' : 'Chemical', 'value' : 'Chemical'},
                            {'label' : 'Chestnut', 'value' : 'Chestnut'},
                            {'label' : 'Citrus', 'value' : 'Citrus'},
                            {'label' : 'Coffee', 'value' : 'Coffee'},
                            {'label' : 'Diesel', 'value' : 'Diesel'},
                            {'label' : 'Earthy', 'value' : 'Earthy'},
                            {'label' : 'Flowery', 'value' : 'Flowery'},
                            {'label' : 'Fruit', 'value' : 'Fruit'},
                            {'label' : 'Grape', 'value' : 'Grape'},
                            {'label' : 'Grapefruit', 'value' : 'Grapefruit'},
                            {'label' : 'Honey', 'value' : 'Honey'},
                            {'label' : 'Lavender', 'value' : 'Lavender'},
                            {'label' : 'Lemon', 'value' : 'Lemon'},
                            {'label' : 'Lime', 'value' : 'Lime'},
                            {'label' : 'Mango', 'value' : 'Mango'},
                            {'label' : 'Menthol', 'value' : 'Menthol'},
                            {'label' : 'Mint', 'value' : 'Mint'},
                            {'label' : 'Minty', 'value' : 'Minty'},
                            {'label' : 'None.1', 'value' : 'None.1'},
                            {'label' : 'Nutty', 'value' : 'Nutty'},
                            {'label' : 'Orange', 'value' : 'Orange'},
                            {'label' : 'Peach', 'value' : 'Peach'},
                            {'label' : 'Pear', 'value' : 'Pear'},
                            {'label' : 'Pepper', 'value' : 'Pepper'},
                            {'label' : 'Pine', 'value' : 'Pine'},
                            {'label' : 'Pineapple', 'value' : 'Pineapple'},
                            {'label' : 'Pungent', 'value' : 'Pungent'},
                            {'label' : 'Rose', 'value' : 'Rose'},
                            {'label' : 'Sage', 'value' : 'Sage'},
                            {'label' : 'Skunk', 'value' : 'Skunk'},
                            {'label' : 'Spicy/Herbal', 'value' : 'Spicy/Herbal'},
                            {'label' : 'Strawberry', 'value' : 'Strawberry'},
                            {'label' : 'Sweet', 'value' : 'Sweet'},
                            {'label' : 'Tar', 'value' : 'Tar'},
                            {'label' : 'Tea', 'value' : 'Tea'},
                            {'label' : 'Tobacco', 'value' : 'Tobacco'},
                            {'label' : 'Tree', 'value' : 'Tree'},
                            {'label' : 'Tropical', 'value' : 'Tropical'},
                            {'label' : 'Vanilla', 'value' : 'Vanilla'},
                            {'label' : 'Violet', 'value' : 'Violet'},
                            {'label' : 'Woody', 'value' : 'Woody'}
                        ], value='None.1' )
                    ],className='col-4'),
                    html.Div([
                        html.P('Flavor3 : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputFlavor3', options=[
                            {'label' : 'Ammonia', 'value' : 'Ammonia'},
                            {'label' : 'Apple', 'value' : 'Apple'},
                            {'label' : 'Apricot', 'value' : 'Apricot'},
                            {'label' : 'Berry', 'value' : 'Berry'},
                            {'label' : 'Blue', 'value' : 'Blue'},
                            {'label' : 'Blueberry', 'value' : 'Blueberry'},
                            {'label' : 'Butter', 'value' : 'Butter'},
                            {'label' : 'Cheese', 'value' : 'Cheese'},
                            {'label' : 'Chemical', 'value' : 'Chemical'},
                            {'label' : 'Chestnut', 'value' : 'Chestnut'},
                            {'label' : 'Citrus', 'value' : 'Citrus'},
                            {'label' : 'Coffee', 'value' : 'Coffee'},
                            {'label' : 'Diesel', 'value' : 'Diesel'},
                            {'label' : 'Earthy', 'value' : 'Earthy'},
                            {'label' : 'Flowery', 'value' : 'Flowery'},
                            {'label' : 'Fruit', 'value' : 'Fruit'},
                            {'label' : 'Grape', 'value' : 'Grape'},
                            {'label' : 'Grapefruit', 'value' : 'Grapefruit'},
                            {'label' : 'Honey', 'value' : 'Honey'},
                            {'label' : 'Lavender', 'value' : 'Lavender'},
                            {'label' : 'Lemon', 'value' : 'Lemon'},
                            {'label' : 'Lime', 'value' : 'Lime'},
                            {'label' : 'Mango', 'value' : 'Mango'},
                            {'label' : 'Menthol', 'value' : 'Menthol'},
                            {'label' : 'Mint', 'value' : 'Mint'},
                            {'label' : 'Minty', 'value' : 'Minty'},
                            {'label' : 'None.1', 'value' : 'None.1'},
                            {'label' : 'Nutty', 'value' : 'Nutty'},
                            {'label' : 'Orange', 'value' : 'Orange'},
                            {'label' : 'Peach', 'value' : 'Peach'},
                            {'label' : 'Pear', 'value' : 'Pear'},
                            {'label' : 'Pepper', 'value' : 'Pepper'},
                            {'label' : 'Pine', 'value' : 'Pine'},
                            {'label' : 'Pineapple', 'value' : 'Pineapple'},
                            {'label' : 'Pungent', 'value' : 'Pungent'},
                            {'label' : 'Rose', 'value' : 'Rose'},
                            {'label' : 'Sage', 'value' : 'Sage'},
                            {'label' : 'Skunk', 'value' : 'Skunk'},
                            {'label' : 'Spicy/Herbal', 'value' : 'Spicy/Herbal'},
                            {'label' : 'Strawberry', 'value' : 'Strawberry'},
                            {'label' : 'Sweet', 'value' : 'Sweet'},
                            {'label' : 'Tar', 'value' : 'Tar'},
                            {'label' : 'Tea', 'value' : 'Tea'},
                            {'label' : 'Tobacco', 'value' : 'Tobacco'},
                            {'label' : 'Tree', 'value' : 'Tree'},
                            {'label' : 'Tropical', 'value' : 'Tropical'},
                            {'label' : 'Vanilla', 'value' : 'Vanilla'},
                            {'label' : 'Violet', 'value' : 'Violet'},
                            {'label' : 'Woody', 'value' : 'Woody'}
                        ], value='None.1' )
                    ],className='col-4'),
                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])




            