import requests
import json
import pandas as pd
#import weasyprint

pd.set_option('display.max_colwidth',100)

api_key = '40aeabbebadefd6161506467c8474b50'
LVD_url = 'https://stats.lf8.nl/index.php?module=API&method=Live.getLastVisitsDetails&idSite=1&period=day&date=yesterday&format=JSON&token_auth='+ api_key

lvd = requests.get(LVD_url)
ad = requests.get(LVD_url)
data_lvd = json.loads(lvd.content)
df_lvd = pd.DataFrame(data_lvd)
df_lvd = df_lvd.iloc[:,[20,25,30,46,47,49,51,58,72,85]]
df_lvd = df_lvd.set_index(df_lvd.columns[0])
#df_lvd.drop(['actionDetails'], axis=1,inplace=True)

data_ad = json.loads(ad.content)
df_ad = pd.DataFrame(data_ad)
df_ad = df_ad.iloc[:,[5,20]]
df_ad = df_ad.set_index(df_ad.columns[1])

idx = 1


actionDetails = df_ad.iloc[idx,0]
df_actionDetails = pd.DataFrame(actionDetails)
df_actionDetails = df_actionDetails.iloc[:,[0,1,7,12,16]]
df_actionDetails['userid'] = df_lvd.index[idx]
df_actionDetails = df_actionDetails.set_index('userid')

#df_lvd.head()
#df_ad.head()
df_actionDetails..head()

