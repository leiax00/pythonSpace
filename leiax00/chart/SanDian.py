# coding: utf-8
import xlrd
from matplotlib.colors import LogNorm, PowerNorm
import matplotlib.pyplot as plt
import numpy as np

# normal distribution center at x=0 and y=5
# excel = xlrd.open_workbook(r'c:\Users\leiax00\Desktop\XB1.xlsx')
# xls_sheet = excel.sheet_by_index(0)
# y = xls_sheet.col_values(0)[1:]
# x = xls_sheet.col_values(1)[1:]
# gammas = [0.8, 0.5, 0.3]
# # plt.hist2d(x, y, bins=40, norm=LogNorm())
# plt.hist2d(x, y, bins=80, norm=PowerNorm(0.2))
# plt.colorbar()
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import xlrd as xlrd
from numpy.random import multivariate_normal

data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
])

gammas = [0.8, 0.5, 0.3]

# fig, axes = plt.subplots(nrows=2, ncols=2)
excel = xlrd.open_workbook(r'c:\Users\leiax00\Desktop\XB1.xlsx')
xls_sheet = excel.sheet_by_index(0)
y = xls_sheet.col_values(0)[1:]
x = xls_sheet.col_values(1)[1:]
# axes[0, 0].set_title('Linear normalization')
plt.hist2d(x, y, bins=200, norm=mcolors.PowerNorm(0.1))

# for ax, gamma in zip(axes.flat[1:], gammas):
#     ax.set_title('Power law $(\gamma=%1.1f)$' % gamma)
#     ax.hist2d(x, y,
#               bins=100, norm=mcolors.PowerNorm(gamma))

# fig.tight_layout()

plt.show()