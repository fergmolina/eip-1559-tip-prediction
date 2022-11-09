from duneanalytics import DuneAnalytics
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

dune = DuneAnalytics(os.getenv('DUNE_USER'), os.getenv('DUNE_PASSWORD'))

dune.login()

dune.fetch_auth_token()


result_id = dune.query_result_id(query_id=1535489)
data = dune.query_result(result_id)
data = [d['data'] for d in [{k: v for k, v in d.items() if k == 'data'} for d in data['data']['get_result_by_result_id']]]
df_blocks = pd.DataFrame(data)

result_id = dune.query_result_id(query_id=1536052)
data = dune.query_result(result_id)
data = [d['data'] for d in [{k: v for k, v in d.items() if k == 'data'} for d in data['data']['get_result_by_result_id']]]
df_blocks2 = pd.DataFrame(data)

df_blocks = df_blocks.append(df_blocks2, ignore_index=True)


df_blocks.to_csv('bsc.csv')