#%%
import numpy as np
from openpyxl import Workbook
from openpyxl.chart import (ScatterChart,Reference,Series)

wb = Workbook()
ws = wb.active

t = np.linspace(0,100,101)
y = np.sin(t)
t2 = np.linspace(0,100,1001)
y2 = np.cos(t2)

maxlen = max(len(t),len(y),len(t2),len(y2))
data = np.empty((maxlen,4))
#%%
tlist = t.tolist()
ylist = y.tolist()
t2list = t2.tolist()
y2list = y2.tolist()

# %%
data = []
for i in range(maxlen):
    try :
        tempt = tlist[i]
        tempy = ylist[i]
    except IndexError:
        tempt = ''
        tempy = ''
    ws.append([tempt,tempy,t2list[i],y2list[i]])
# %%
chart = ScatterChart()
xvalues = Reference(ws,min_col=1,min_row=1,max_row=100)
yvalues = Reference(ws,min_col=2,min_row=1,max_row=100)
series = Series(yvalues,xvalues)
chart.series.append(series)

xvalues = Reference(ws,min_col=3,min_row=1,max_row=200)
yvalues = Reference(ws,min_col=4,min_row=1,max_row=200)
series = Series(yvalues,xvalues)
chart.series.append(series)

# %%
ws.add_chart(chart)

# %%
wb.save("temp.xlsx")
# %%
