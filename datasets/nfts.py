import requests
import datetime
import pandas as pd

nft = pd.DataFrame(columns=['timestamp'])
i=0

# bored-ape-yacht-club
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/bored-ape-yacht-club/charts/all")
response_json = response.json()
collection = 'bayc'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft = nft.append({'timestamp': formated_date}, ignore_index=True)
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1


# cryptopunks
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/cryptopunks/charts/all")
response_json = response.json()
collection = 'cp'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# mutant-ape-yacht-club
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/mutant-ape-yacht-club/charts/all")
response_json = response.json()
collection = 'mayc'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# autoglyphs
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/autoglyphs/charts/all")
response_json = response.json()
collection = 'agp'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# chromie-squiggle-art-blocks-curated
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/chromie-squiggle-art-blocks-curated/charts/all")
response_json = response.json()
collection = 'csabc'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# fidenza-art-blocks-curated
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/fidenza-art-blocks-curated/charts/all")
response_json = response.json()
collection = 'fabc'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# azuki
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/azuki/charts/all")
response_json = response.json()
collection = 'azuki'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# proof-moonbirds
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/proof-moonbirds/charts/all")
response_json = response.json()
collection = 'mbirds'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# doodles
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/doodles/charts/all")
response_json = response.json()
collection = 'doodles'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# ringers-art-blocks-curated
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/ringers-art-blocks-curated/charts/all")
response_json = response.json()
collection = 'rabc'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# meebits
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/meebits/charts/all")
response_json = response.json()
collection = 'meebits'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# pudgy-penguins
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/pudgy-penguins/charts/all")
response_json = response.json()
collection = 'pp'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# cool-cats
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/cool-cats/charts/all")
response_json = response.json()
collection = 'ccats'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# world-of-women
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/world-of-women/charts/all")
response_json = response.json()
collection = 'wow'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# goblintownwtf
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/goblintownwtf/charts/all")
response_json = response.json()
collection = 'goblin'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# cryptodickbutts
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/cryptodickbutts/charts/all")
response_json = response.json()
collection = 'cdb'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# mfers
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/mfers/charts/all")
response_json = response.json()
collection = 'mfers'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# deadfellaz
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/deadfellaz/charts/all")
response_json = response.json()
collection = 'deadfellaz'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# beeple-everydays
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/beeple-everydays/charts/all")
response_json = response.json()
collection = 'beeple'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

# clonex
i=0
last_date = ''
response = requests.get("https://api-bff.nftpricefloor.com/projects/clonex/charts/all")
response_json = response.json()
collection = 'clonex'
nft[collection+'_floor_usd'] = 0
nft[collection+'_volume_usd'] = 0
nft[collection+'_sales_count'] = 0
for date in response_json['timestamps']:
    #print(datetime.datetime.utcfromtimestamp(date / 1e3).date())
    formated_date = datetime.datetime.utcfromtimestamp(date / 1e3).date()
    if last_date != formated_date:
        nft.at[nft['timestamp'] ==  formated_date,collection+'_floor_usd'] = response_json['floorUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_volume_usd'] = response_json['volumeUsd'][i]
        nft.at[nft['timestamp'] ==  formated_date,collection+'_sales_count'] = response_json['salesCount'][i]
        last_date = formated_date
    i = i + 1

print(nft)

nft.to_csv('nft.csv') 


