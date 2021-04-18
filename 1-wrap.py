import pandas as pd
import numpy as np
import updategoogle
import workshop_update
from plan2 import plan2 
import os
from data import order
workshop = ('BK','AW')
person = (80,200)
i = 1
a = workshop_update.producelist4(order,workshop[i])
# a = a[a.cap.notna()]
b= plan2(a,person[i],schedulerange=100,customer_prior1=[],ketqua=2)
a['confirm_etd'] = a['confirm_etd'].dt.strftime('%Y-%m-%d')
a['production_date'] = a['production_date'].dt.strftime('%y-%m-%d')
# c= a.values.tolist()
pd.options.display.float_format = '{:1,}'.format
updategoogle.google_pandas(b,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop[i],'AK4')
print(a.dtypes)
a.to_excel('BK.xlsx')
os.system('BK.xlsx')
# updategoogle.google_pandas(a,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop[i],'C4')
