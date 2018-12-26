import os
import numpy as np
import pandas as pd

# losowanie
df_sample = df.sample(n=None, frac=0.1)

def conversion_ind(df):
    return round(df['Class'].sum() / len(df['Class']), 4)

conversion_ind(df)
conversion_ind(df_sample)

# analiza różnych typów kolumn
df2 = pd.DataFrame([['jeden','jeden','dwa','trzy','jeden','dwa','dwa'],[25,40,26,30,26,20,25],[1,0,0,1,1,0,1],[1,1,0,1,0,0,1]]).T
df2.columns = ['Pierwsza','Druga','Trzecia','Class']
df2
conversion(df2)

#df2.groupby([df2.columns[1]])[df2.columns[-1]].sum()
#df2.groupby(['Pierwsza','Trzecia'])[['Class']].sum()
def grouping(df_name, column_name, top_n=3, group_cnt=0, conv_threshold=0):
    df_name = df_name.copy()
    df_name['Class_cnt'] = df_name['Class']
    df_grouped = df_name.groupby([column_name]).agg({'Class': 'sum', 'Class_cnt': 'count' })
    df_grouped['Conversion'] = round(df_grouped['Class'] / df_grouped['Class_cnt'], 4)
    df_grouped = df_grouped.drop(['Class'], axis=1)
    df_grouped = df_grouped[df_grouped['Class_cnt'] >= group_cnt ]
    df_grouped = df_grouped[df_grouped['Conversion'] >= conv_threshold ]
    df_grouped = df_grouped.sort_values(by='Conversion', ascending=True).iloc[:top_n]
    print(df_grouped)

for col_name in df_sample.columns[:5]:
    grouping(df_sample, col_name, None, 0, 0)
