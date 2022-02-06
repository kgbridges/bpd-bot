import requests
import pandas as pd

# Pull data from ArcGIS API

url = "https://services.arcgis.com/ePKBjXrBZ2vEEgWd/arcgis/rest/services/BPD_Offenses/FeatureServer/0/query?where=1%3D1&outFields=Report_Number,Report_Date&returnGeometry=false&returnCountOnly=false&outSR=4326&f=json"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

results = []
for _feature in data['features']:
    results.append(_feature['attributes'])

# Create DataFrame
df = pd.json_normalize(results)

print(df)
