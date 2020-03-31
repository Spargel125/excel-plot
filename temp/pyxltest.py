#%%
import numpy as np
from openpyxl import Workbook
from openpyxl.chart import (ScatterChart,Reference,Series)

wb = Workbook()
ws = wb.active

t = np.linspace(0,100,101)
y = np.sin(t)
#%%
tlist = t.tolist()
ylist = y.tolist()
# %%
data = []
for i in range(len(t)):
    ws.append([tlist[i],ylist[i]])
# %%
wb.save("temp.xlsx")
# %%
