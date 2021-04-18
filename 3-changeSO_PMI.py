from to_excel2 import load_excel_contain
from getdatafromSO import so
import pandas as pd
import os
UPG = 'E:\Happychews\Colab\data\shipping\PMI20210222.xlsx'
sheet = 'HC '
# sửa lại ngày confirm
contain = ['P-Code','PO#','Received','ITEM','(EA)','Feb-22th','REMARK']
renamecolumn = ['p-code ','po','receive_date','item','qty','confirm_etd','remark']

a = load_excel_contain(UPG,sheet,contain,renamecolumn,skiprow=0)
a= a[~a.po.isna()]
a['po'] = a.po.apply(lambda x: str(int(x)))
df= a.merge(so,how='left',on=['po','item'],)
# df['different'] = df['confirm_etd_y'] - df['confirm_etd_x']
df.to_excel('test_PMI.xlsx')
os.system('test_PMI.xlsx')
print(df.dtypes)