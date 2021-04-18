from getdatafromSO import so
import pandas as pd
from updategoogle import google_value_row_index,getsinglecellvalue_rowindex
import time
import numpy as np


spreadsheet_url = '1ejYQsDucZN1mDbwGNE1YW2oUE1S9xsbwiUsGr3zXsCk'
sheet = 'SO'
fix_path ='E:\Happychews\Colab\data\shipping\Fix_ETD_UPG.xlsx'
a= pd.read_excel(fix_path,sheet_name='Sheet1',engine='openpyxl')
etd = a['confirm_etd_x'].to_numpy(dtype=str)
for index in a.index:
    row = a['row'][index]
    po2 = str(a['po'][index])
    item2= a['item'][index]
    po = str(getsinglecellvalue_rowindex(spreadsheet_url,sheet,row,6))
    item = getsinglecellvalue_rowindex(spreadsheet_url,sheet,row,7)
    if po2==po and item2==item:
        google_value_row_index(spreadsheet_url,sheet,row,2,etd[index])
        print(f'update {po} {item} in {row}: ')
    else:
        print(f'WRONG PO& ITEM!!!!! {po} {item} in {row}: ')
    time.sleep(2)
