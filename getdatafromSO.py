from updategoogle import getdatafromgooglesheet
import pandas as pd
from datetime import datetime

spreadsheet_url = '1ejYQsDucZN1mDbwGNE1YW2oUE1S9xsbwiUsGr3zXsCk'
sheet = 'SO'

a = getdatafromgooglesheet(spreadsheets_url=spreadsheet_url, sheet=sheet, range='C1:I')
so = pd.DataFrame(data=a.iloc[1:,:].values,columns=a.iloc[0,:])
so.columns = ['customer','so','mnf','po','item','qty','confirm_etd']
so['row_number'] = so['po'].index+2
so= so[~so['po'].isna()]
so['qty'] = so['qty'].apply(lambda x: int(x.replace(',','')))
 
so['confirm_etd'] = so['confirm_etd'].apply(lambda x: datetime.strptime(x,'%m/%d/%Y'))
# print(so['confirm_etd'])
if __name__ == '__main__':
    print(so['row_number'])
    print(so.dtypes)
    import os
    so.to_excel('so.xlsx')
    os.system('so.xlsx')