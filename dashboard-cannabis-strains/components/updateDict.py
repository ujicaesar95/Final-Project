import pandas as pd


def updateDict(Effects1,Effects2,Effects3,Effects4,Effects5, Flavor1,Flavor2,Flavor3) :

    dictio={
        'Aroused':0,
        'Creative':0,
        'Dry' : 0,
        'Energetic' : 0,
        'Euphoric' : 0,
        'Focused' : 0,
        'Giggly' : 0,
        'Happy' : 0,
        'Hungry' : 0,
        'None' : 0,
        'Relaxed' : 0,
        'Sleepy' : 0,
        'Talkative' : 0,
        'Tingly' : 0,
        'Uplifted' : 0,
        'Ammonia':0,
        'Apple':0,
        'Apricot':0,
        'Berry':0,
        'Blue':0,
        'Blueberry':0,
        'Butter':0,
        'Cheese':0,
        'Chemical':0,
        'Chestnut':0,
        'Citrus':0,
        'Coffee':0,
        'Diesel':0,
        'Earthy':0,
        'Flowery':0,
        'Fruit':0,
        'Grape':0,
        'Grapefruit':0,
        'Honey':0,
        'Lavender':0,
        'Lemon':0,
        'Lime':0,
        'Mango':0,
        'Menthol':0,
        'Mint':0,
        'Minty':0,
        'None.1':0,
        'Nutty':0,
        'Orange':0,
        'Peach':0,
        'Pear':0,
        'Pepper':0,
        'Pine':0,
        'Pineapple':0,
        'Pungent':0,
        'Rose':0,
        'Sage':0,
        'Skunk':0,
        'Spicy/Herbal':0,
        'Strawberry':0,
        'Sweet':0,
        'Tar':0,
        'Tea':0,
        'Tobacco':0,
        'Tree':0,
        'Tropical':0,
        'Vanilla':0,
        'Violet':0,
        'Woody':0
        }
    dictio[Effects1]=1
    dictio[Effects2]=1
    dictio[Effects3]=1
    dictio[Effects4]=1
    dictio[Effects5]=1
    dictio[Flavor1]=1
    dictio[Flavor2]=1
    dictio[Flavor3]=1

    return dictio