import gspread
import pandas as pd
import numpy as np
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'eveni-database-4ecde3632479.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials).open('[eveni] 지원팀 데이터')




#https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ko&project=프로젝트명
#key 발급 -> 

data= gc.worksheet('시트3')
records_data = data.get_all_records()
records_df = pd.DataFrame.from_dict(records_data)
records_df["시간"] = records_df["시간"].astype(str)
records_df = records_df.replace('', np.NaN)
# view the top records
records_df.rename(columns = {'컨설팅일자':'class_date', '시간':'class_time', '컨설턴트':'consultant', '고객명':'student','예정/완료':'is_done'}, inplace = True)


credentials = service_account.Credentials.from_service_account_file(json_file_name)
records_df.to_gbq('eveni.test', project_id='eveni-database', chunksize=None, reauth=False , if_exists='fail', credentials = credentials)

#query = "SELECT * FROM `dataset.table`"
#df = pd.read_gbq(query=query, project_id="project_id", credentials=credentials, dialect='standard')
# 'fail'
# If table exists raise pandas_gbq.gbq.TableCreationError.

# 'replace'
# If table exists, drop it, recreate it, and insert data.

# 'append'
# If table exists, insert data. Create if does not exist.
                  
