from duneanalytics import DuneAnalytics
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

dune = DuneAnalytics(os.getenv('DUNE_USER'), os.getenv('DUNE_PASSWORD'))

dune.login()

dune.fetch_auth_token()


##### Utilization Rate #####
result_id = dune.query_result_id(query_id=1544849)
# fetch query result
data = dune.query_result(result_id)
data = [d['data'] for d in [{k: v for k, v in d.items() if k == 'data'} for d in data['data']['get_result_by_result_id']]]
df_hourly = pd.DataFrame(data)

df_hourly.to_csv('utilization_rate.csv')