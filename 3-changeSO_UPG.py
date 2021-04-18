from to_excel2 import load_excel_contain
from getdatafromSO import so
import pandas as pd
import os
workbook = 'E:\Happychews\Colab\data\shipping\Meg20210222.xlsx'
sheet = 'orders'
contain = ['Eric','PO#','Received','ITEM','(EA)','Current']
renamecolumn = ['p-code ','po','receive_date','item','qty','confirm_etd']

a = load_excel_contain(workbook,sheet,contain,renamecolumn,skiprow=0)
a= a[~a.po.isna()]
print(a.columns)
a['po'] = a.po.apply(lambda x: str(int(x)))
df= a.merge(so,how='left',on=['po','item'],)
#df['different'] = df['confirm_etd_y'] - df['confirm_etd_x']
df.to_excel('test.xlsx')
os.system('test.xlsx')
# print(df.dtypes)