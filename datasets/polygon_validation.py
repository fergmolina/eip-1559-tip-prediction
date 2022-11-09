from duneanalytics import DuneAnalytics
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

dune = DuneAnalytics(os.getenv('DUNE_USER'), os.getenv('DUNE_PASSWORD'))

dune.login()

dune.fetch_auth_token()


result_id = dune.query_result_id(query_id=1536611)
# fetch query result
data = dune.query_result(result_id)
data = [d['data'] for d in [{k: v for k, v in d.items() if k == 'data'} for d in data['data']['get_result_by_result_id']]]
df_blocks = pd.DataFrame(data)

print(df_blocks)

result_id = dune.query_result_id(query_id=1536626)
data = dune.query_result(result_id)
data = [d['data'] for d in [{k: v for k, v in d.items() if k == 'data'} for d in data['data']['get_result_by_result_id']]]
df_tips = pd.DataFrame(data)


df_total=pd.merge(df_blocks,df_tips, how='left', left_on='block_time', right_on='block_time')
print(df_total)

df_total.to_csv('polygon_validation.csv')