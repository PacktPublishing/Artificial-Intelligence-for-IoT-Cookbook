import pandas as pd 

df = pd.read_csv('Beach_Water_Quality_-_Automated_Sensors.csv', header=0)

df = df[df['Beach Name'] ==   'Rainbow Beach']
df = df[df['Water Temperature'] >  -100]
df = df[df['Wave Period'] >  -100]
df['Measurement Timestamp'] =pd.to_datetime(df['Measurement Timestamp'])

Turbidity = df[['Measurement Timestamp', 'Turbidity']]
Turbidity.to_csv('Turbidity.csv', index=False, header=False)