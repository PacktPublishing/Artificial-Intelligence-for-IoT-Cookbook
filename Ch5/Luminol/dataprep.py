import pandas as pd 

df = pd.read_csv('Ch5/Luminol/Beach_Water_Quality_-_Automated_Sensors.csv', header=0)

df = df[df['Beach Name'] ==   'Rainbow Beach']
df = df[df['Water Temperature'] >  -100]
df = df[df['Wave Period'] >  -100]
df['Measurement Timestamp'] = pd.Timestamp(df['Measurement Timestamp'])
print(df.count())
print('done')


print(df)