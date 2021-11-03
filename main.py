import requests
import requests
res=requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/GE?serietype=line&apikey=79cc96e2b0ac1afdd43138fc093b7bde")
### Print Response Status Code
print(res.status_code)
### Print Response Status Code
print(res.json())

file=open("./+GE+.json", "w+")
file.writelines(res.text)
file.close()

import requests
res=requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line&apikey=79cc96e2b0ac1afdd43138fc093b7bde")
### Print Response Status Code
print(res.status_code)
### Print Response Status Code
print(res.json())

file=open("./+AAPL+.json", "w+")

file.writelines(res.text)

file.close()


import requests
res=requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/GM?serietype=line&apikey=79cc96e2b0ac1afdd43138fc093b7bde")
### Print Response Status Code
print(res.status_code)
### Print Response Status Code
print(res.json())

file=open("./+GM+.json", "w+")

file.writelines(res.text)

file.close()

import pandas as pd
aaplDataframe= pd.read_json("+AAPL+.json")

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')










