

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import binascii
from datetime import datetime

# importing data from website
url = 'http://sbsrv1.cs.nuim.ie/lora/list.php?node=a8610a32331f860d&format=json'
df = pd.read_json(url, dtype= object)
da = df
da = da[0:0]
# sorting the data from hex to ascii
for i in range(len(df.data)):
    #df['decoded'][i] = binascii.unhexlify(data1[i]) # changing from hex to ascii
    df.at[i, 'data'] = binascii.unhexlify(df.at[i, 'data'])

#choosing the first 50 columes
df = df.loc[0:len(df),['ts', 'data']]
da = da[['ts', 'data']]

# getting data from a certain date
for i in range(len(df.ts)):
    when = df.at[i, 'ts']
    when = when[0:13]
    df.at[i, 'ts'] = datetime.strptime(when, '%Y-%m-%d %H')



dateFilter = datetime.strptime('2019-04-10 14', '%Y-%m-%d %H')
j = 0
for i in range(len(df)):
    dateSelect = df.at[i, 'ts']

    if (dateSelect < dateFilter):

         j = i
         break


df = df[0:j]
#print(da)




# splitting data received to temp and moisture than converting it from string to ints
df[['S_moisture','10cm_under', 'Airtemp']] = df['data'].str.split(" ", n=2, expand=True)



# adding to data frame
df = df[['ts','S_moisture','10cm_under', 'Airtemp']]

#print(df)

# reversing the order of the data
df.iloc[:] = df.iloc[::-1].values
print(df)

plt.plot(df['ts'], df['S_moisture'])
plt.plot(df['ts'], df['10cm_under'])

plt.tick_params(axis='x',labelrotation=90)
plt.grid(True)
plt.show()


#print(df)

