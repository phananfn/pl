import pandas as pd
import os
### order
#E:\Happychews\Colab\data\order\order.csv
order = pd.read_csv('E:\Happychews\Colab\data/order/order.csv',parse_dates=['confirm_etd','production_date','packing_date','colorbag_available'],thousands=',') 
### report
report = pd.read_csv('E:\Happychews\Colab\data/report/report.csv',parse_dates=['p_date']) 
### schedule 
schedule_csv='E:\Happychews\Colab\data\schedule\schedule.xls'
schedule = pd.read_excel(schedule_csv,parse_dates=['schedule_date'],dtype={'worktime':float},sheet_name='Sheet1')

order = order[~order.po.isna()]
#### 
