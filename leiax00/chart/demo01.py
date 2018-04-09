# coding：utf-8
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
import xlrd

np.random.seed(19680801)

excel = xlrd.open_workbook(r'c:\Users\leiax00\Desktop\XB1.xlsx')
xls_sheet = excel.sheet_by_index(0)
y = xls_sheet.col_values(0)[1:]
x = xls_sheet.col_values(1)[1:]
print('x', x)
list.sort(x)
print(x)
print('y', y)
list.sort(y)
print(y)
xmin = x[0]
xmax = x[-1]
ymin = y[0]
ymax = y[-1]

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(7, 4))
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
ax = axs[0]
hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.axis([xmin, xmax, ymin, ymax])
ax.set_title("Hexagon binning")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')

ax = axs[1]
hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.axis([xmin, xmax, ymin, ymax])
ax.set_title("With a log color scale")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log10(N)')

plt.show()