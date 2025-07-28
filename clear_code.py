import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bar_chart_race as bcr

with open("result.json", 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

names = []
for i in range(1, len(data["messages"])):
    if data["messages"][i]["type"] == 'message':
        names.append([data["messages"][i]["from"], data["messages"][i]["date"][:10]])

data2 = []
counter = {}
for i, [name, date] in enumerate(names):
    counter[name] = counter.get(name, 0) + 1
    if i != len(names) - 1:
        if date != names[i+1][1]:
            row = counter.copy()
            data2.append(row)
    else: 
        row = counter.copy()
        data2.append(row)
            

df = pd.DataFrame(data2).fillna(0).astype(int)
df.index = [f'Шаг {i+1}' for i in range(len(df))]

bcr.bar_chart_race(
    df=df,
    filename='race.gif',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=5,
    interpolate_period=True,
    period_length= 100,
    period_label={'x': .99, 'y': .1, 'ha': 'right', 'va': 'center'},
    title='Количество сообщений',
    bar_size=.95,
    cmap='dark12'
)
