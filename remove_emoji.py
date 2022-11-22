import pandas as pd
df = pd.read_excel('서울시 마들렌 맛집] 리뷰 (1018).xlsx')
df = df.drop(columns=['Unnamed: 0'])
df

pip install emoji

from emoji import core

for name in df.columns:
    for i in range(200):
        text = df[name][i]
        s = core.replace_emoji(text, replace="")
        df[name][i] = s
df