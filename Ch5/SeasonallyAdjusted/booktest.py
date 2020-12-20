import pandas as pd 
import numpy as np

df = pd.read_csv('Beach_Water_Quality_-_Automated_Sensors.csv', header=0)
df = df[df['Beach Name'] == 'Rainbow Beach']
df = df[df['Water Temperature'] > -100]
df = df[df['Wave Period'] > -100]
waveheight = df[['Wave Height']].to_numpy()
