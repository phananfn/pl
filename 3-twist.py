import pandas as pd
import numpy as np
import updategoogle
import workshop_update
from plan2 import plan2 
from data import order
import os
workshop = 'BT'
person = 60
a = workshop_update.producelist3(order,workshop)
b= plan2(a,person,schedulerange=100,customer_prior1=[],ketqua=2)
a['confirm_etd'] = a['confirm_etd'].dt.strftime('%Y-%m-%d')
a['production_date'] = a['production_date'].dt.strftime('%y-%m-%d')
# c= a.values.tolist()
pd.options.display.float_format = '{:1,}'.format
updategoogle.google_pandas(b,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop,'AF4')
a.to_excel(workshop+'.xlsx')
os.system(workshop+'.xlsx')
print(b,a.shape)
# updategoogle.google_pandas(a,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop,'C4')
