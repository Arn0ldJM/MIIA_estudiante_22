# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:45:18 2021

@author: Arnold
"""

#%%
# Ejercicio 1

import plotly.graph_objects as go
import ipywidgets as widgets
import pandas as pd
from ipywidgets import interactive


df = pd.read_csv('Archivos/BankChurners.csv')
df.head()

print(df["Marital_Status"].value_counts())

fig = go.Figure(data=[go.Pie(labels=[], values=[], pull=[0.2, 0, 0, 0])])
fig.show()
