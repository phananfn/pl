import pandas as pd
import numpy as np
import updategoogle
import workshop_update
from plan5 import plan5 
from data import order
import os

a = workshop_update.orderlist(order)
# a['cbm'][a.cbm==0]=0.02
# b= plan5(a,220,schedulerange=100,customer_prior1=['VO','WM','PTC','KTR'],customer_prior2=['VO','UPG','PMI'],customer_prior3=['VO','UPG','PMI'],ketqua=1)
# a['confirm_etd'] = a['confirm_etd'].dt.strftime('%Y-%m-%d')
# a['packing_date'] = a['production_date'].dt.strftime('%y-%m-%d')
# print(a['colorbag_available'].dtypes)
# c= a.values.tolist()
# updategoogle.google_pandas(a,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop[i],'C4')
# pd.options.display.float_format = '{:1,}'.format
# updategoogle.google_pandas(b,'1t4sNjb0v5BpU7lu6DkPMUbms3l7Dt9baoCU2kzl3t4k',workshop[i],'AF4')
# print(a.dtypes)
# print(b.size,a.shape)
a.to_excel('orderlist.xlsx')
