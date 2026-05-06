import pandas as pd

t = pd.read_html("https://en.wikipedia.org/wiki/Nuclear_power_plant")
print(len(t))
print(t[0].head())
    