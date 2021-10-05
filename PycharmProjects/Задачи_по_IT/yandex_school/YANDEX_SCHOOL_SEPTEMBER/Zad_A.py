import pandas as pd
# Chtenie faila JSON

dictData=pd.read_json("DATA_ZAD_A.txt")
print(dictData)

# real_count= count-return_count if real_count <0: real_count=0
# 1 Uslovie if status == 'CANCEL':

dictData = dictData.sort_values(by='event_id')
print(dictData)
print(dictData)
print(dictData.groupby(['order_id'], as_index=False))
