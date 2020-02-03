import pandas as pd 
import sesd
import numpy as np

df = pd.read_csv('Beach_Water_Quality_-_Automated_Sensors.csv', header=0)
df = df[df['Beach Name'] == 'Rainbow Beach']
df = df[df['Water Temperature'] > -100]
df = df[df['Wave Period'] > -100]
waveheight = df[['Wave Height']].to_numpy()

outliers_indices = sesd.seasonal_esd(waveheight, hybrid=True, max_anomalies=2)
for idx in outliers_indices:
    print("Anomaly index: {}, anomaly value: {}".format(idx, ts[idx]))

