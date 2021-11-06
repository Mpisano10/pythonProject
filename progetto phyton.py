import pandas as pd # edit dataframe
import requests
import json

JSONContent = requests.get("https://api.magicthegathering.io/v1/cards").json()

df =pd.DataFrame(JSONContent["cards"])
df.head(1) #accede alla prima e alla seconda riga del datafram

from pandas.io.json import json_normalize
pd.json_normalize(JSONContent["cards"])

#ultima parte da rivedere

df = df.drop(columns = df.columns[[4,6,7,9,13,16,18,19,20,21,28,27,26,25,23,22]])
df = df.fillna(0)
df.to_csv(r"pythonProject\MGT.csv")

