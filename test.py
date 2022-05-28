import gspread

from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'eveni-database-e469f5582c7f.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials).open('[eveni] 지원팀 데이터')
# spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1p2LpwzwqQYmyNkCEv6lcVLDjOAbr-TnaQZEnoh7-VwA/edit#gid=1048343811'
# doc = gc.open_by_url(spreadsheet_url)
#worksheet = doc.worksheet('시트3')
# range_list = worksheet.range('{범위, 예시 "A1:B1"}')
#     for cell in range_list:
#         values[i].append(cell.value)

data= gc.worksheet('시트3')
records_data = data.get_all_records()

import pandas as pd
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()

from datalab.context import Context
import datalab.storage as storage
import datalab.bigquery as bq
import pandas as pd
from pandas import DataFrame
import time


#Alternative 3
start = time.time()
sample_bucket_name = Context.default().project_id + '-datalab-example'
sample_bucket_path = 'gs://' + sample_bucket_name
sample_bucket_object = sample_bucket_path + '/Hello.txt'
bigquery_dataset_name = 'TestDataSet'
bigquery_table_name = 'TestTable'

# Define storage bucket
sample_bucket = storage.Bucket(sample_bucket_name)

# Create or overwrite the existing table if it exists
table_schema = bq.Schema.from_dataframe(not_so_simple_dataframe)

# Write the DataFrame to GCS (Google Cloud Storage)
%storage write --variable not_so_simple_dataframe --object $sample_bucket_object

# Write the DataFrame to a BigQuery table
table.insert_data(not_so_simple_dataframe)
end = time.time()
print("time alternative 3 " + str(end - start))
