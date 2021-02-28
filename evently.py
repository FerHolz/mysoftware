import requests
import json
import pandas as pd

#api_key = 40aeabbebadefd6161506467c8474b50

serviceurl = 'https://stats.lf8.nl/index.php?module=API&method=Live.getLastVisitsDetails&idSite=1&period=day&date=yesterday&format=JSON&token_auth=40aeabbebadefd6161506467c8474b50'

r = requests.get(serviceurl)
#print('Retrieved', r.url)
data = json.loads(r.content)
#print(data)
#print('Retrieved', len(data), 'dictionary')
df = pd.DataFrame(data)
print(df)

