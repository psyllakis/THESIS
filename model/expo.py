<<<<<<< HEAD
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize
from scipy.optimize import curve_fit
def normalize_data(data):
    return data / np.average(data)


subject_A = [253.61, 224.97, 219.55, 209.49, 188.4, 180.28, 195.29, 190.75, 194.8, 197.96, 193.61, 193.28, 193.16, 180.28, 198.31, 182.99]
axis_A = [0, 1, 1.25, 2, 3, 5, 6, 7, 8, 12, 13, 18, 19, 24, 25, 30]
subject_B = [161.31, 157.85, 166.18, 150.34, 145.33, 146.99, 145.03]
axis_B = [0, 1, 2, 12, 18, 24, 30]
subject_C = [198.99, 198.31, 192.91, 190.99, 194.83, 190.53, 185.59, 178.86, 187.27, 170.33, 168.09, 151.4]
axis_C = [0, 1, 2, 3, 4, 12, 18, 19, 24, 25, 30, 31]
subject_D = [271.41, 268.06, 268.34, 269.33, 266.81, 264.01, 261.83, 258.82, 254.76, 254.44, 252.53, 254.61, 248.72, 251.67, 252.55]
axis_D = [0, 1, 2.52, 3, 4, 5, 6, 7, 8, 12, 18, 19, 22, 24, 30]
subject_E = [155.85, 152.72, 153.36, 134.12, 131.59, 130.25, 127.84]
axis_E = [0, 1, 2, 12, 18, 24, 30]
subject_F = [181.99, 185.18, 177.21, 179.87, 158.16, 165.9, 159.14, 164.1]
axis_F = [0, 1, 2, 3, 4, 11, 12, 18]
subject_G = [196.56, 195.24, 189.99, 182.57, 182.35, 175.75, 136.88, 148.32, 149.93, 140.87, 131.98]
axis_G = [0, 1, 2, 3, 4, 5, 11, 16, 22, 28, 29]
subject_H = [199.92, 189.58, 196.72, 192.04, 182.8, 186.6, 189.96, 185.79]
axis_H = [0, 1, 2, 12, 18, 24, 30, 31]

subject_A = normalize_data(subject_A)
subject_B = normalize_data(subject_B)
subject_C = normalize_data(subject_C)
subject_D = normalize_data(subject_D)
subject_E = normalize_data(subject_E)
subject_F = normalize_data(subject_F)
subject_G = normalize_data(subject_G)
subject_H = normalize_data(subject_H)


# Create a figure with customized size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the axis lables
ax.set_xlabel('Time(min)', fontsize=18)
ax.set_ylabel('Haemoglobin Oxygenation (a.u.)', fontsize=18)


# Line color for error bar
color_subject_A = 'red'
color_subject_B = 'darkgreen'
color_subject_C = 'black'
color_subject_D = 'grey'
color_subject_E = 'blue'
color_subject_F = 'purple'
color_subject_G = 'brown'
color_subject_H = 'orange'
color_subject_k = 'blue'

# Line style for each dataset
lineStyle_subject = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}
minute_0 = []
minute_1 = []
minute_2 = []
minute_3 = []
minute_4 = []
minute_12 = []
minute_18 = []
minute_24 = []
minute_30 = []

axis = [0, 1, 2, 3, 4, 12, 18, 24, 30]
for i in axis:
    if i in axis_A:
        index = axis_A.index(i)
        if i == 0:
            minute_0.append(subject_A[index])
        if i == 1:
            minute_1.append(subject_A[index])
        if i == 2:
            minute_2.append(subject_A[index])
        if i == 3:
            minute_3.append(subject_A[index])
        if i == 4:
            minute_4.append(subject_A[index])
        if i == 12:
            minute_12.append(subject_A[index])
        if i == 18:
            minute_18.append(subject_A[index])
        if i == 24:
            minute_24.append(subject_A[index])
        if i == 30:
            minute_30.append(subject_A[index])
for i in axis:
    if i in axis_B:
        index = axis_B.index(i)
        if i == 0:
            minute_0.append(subject_B[index])
        if i == 1:
            minute_1.append(subject_B[index])
        if i == 2:
            minute_2.append(subject_B[index])
        if i == 3:
            minute_3.append(subject_B[index])
        if i == 4:
            minute_4.append(subject_B[index])
        if i == 12:
            minute_12.append(subject_B[index])
        if i == 18:
            minute_18.append(subject_B[index])
        if i == 24:
            minute_24.append(subject_B[index])
        if i == 30:
            minute_30.append(subject_B[index])
for i in axis:
    if i in axis_C:
        index = axis_C.index(i)
        if i == 0:
            minute_0.append(subject_C[index])
        if i == 1:
            minute_1.append(subject_C[index])
        if i == 2:
            minute_2.append(subject_C[index])
        if i == 3:
            minute_3.append(subject_C[index])
        if i == 4:
            minute_4.append(subject_C[index])
        if i == 12:
            minute_12.append(subject_C[index])
        if i == 18:
            minute_18.append(subject_C[index])
        if i == 24:
            minute_24.append(subject_C[index])
        if i == 30:
            minute_30.append(subject_C[index])
for i in axis:
    if i in axis_D:
        index = axis_D.index(i)
        if i == 0:
            minute_0.append(subject_D[index])
        if i == 1:
            minute_1.append(subject_D[index])
        if i == 2:
            minute_2.append(subject_D[index])
        if i == 3:
            minute_3.append(subject_D[index])
        if i == 4:
            minute_4.append(subject_D[index])
        if i == 12:
            minute_12.append(subject_D[index])
        if i == 18:
            minute_18.append(subject_D[index])
        if i == 24:
            minute_24.append(subject_D[index])
        if i == 30:
            minute_30.append(subject_D[index])
for i in axis:
    if i in axis_E:
        index = axis_E.index(i)
        if i == 0:
            minute_0.append(subject_E[index])
        if i == 1:
            minute_1.append(subject_E[index])
        if i == 2:
            minute_2.append(subject_E[index])
        if i == 3:
            minute_3.append(subject_E[index])
        if i == 4:
            minute_4.append(subject_E[index])
        if i == 12:
            minute_12.append(subject_E[index])
        if i == 18:
            minute_18.append(subject_E[index])
        if i == 24:
            minute_24.append(subject_E[index])
        if i == 30:
            minute_30.append(subject_E[index])
for i in axis:
    if i in axis_F:
        index = axis_F.index(i)
        if i == 0:
            minute_0.append(subject_F[index])
        if i == 1:
            minute_1.append(subject_F[index])
        if i == 2:
            minute_2.append(subject_F[index])
        if i == 3:
            minute_3.append(subject_F[index])
        if i == 4:
            minute_4.append(subject_F[index])
        if i == 12:
            minute_12.append(subject_F[index])
        if i == 18:
            minute_18.append(subject_F[index])
        if i == 24:
            minute_24.append(subject_F[index])
        if i == 30:
            minute_30.append(subject_F[index])
for i in axis:
    if i in axis_G:
        index = axis_G.index(i)
        if i == 0:
            minute_0.append(subject_G[index])
        if i == 1:
            minute_1.append(subject_G[index])
        if i == 2:
            minute_2.append(subject_G[index])
        if i == 3:
            minute_3.append(subject_G[index])
        if i == 4:
            minute_4.append(subject_G[index])
        if i == 12:
            minute_12.append(subject_G[index])
        if i == 18:
            minute_18.append(subject_G[index])
        if i == 24:
            minute_24.append(subject_G[index])
        if i == 30:
            minute_30.append(subject_G[index])
for i in axis:
    if i in axis_H:
        index = axis_H.index(i)
        if i == 0:
            minute_0.append(subject_H[index])
        if i == 1:
            minute_1.append(subject_H[index])
        if i == 2:
            minute_2.append(subject_H[index])
        if i == 3:
            minute_3.append(subject_H[index])
        if i == 4:
            minute_4.append(subject_H[index])
        if i == 12:
            minute_12.append(subject_H[index])
        if i == 18:
            minute_18.append(subject_H[index])
        if i == 24:
            minute_24.append(subject_H[index])
        if i == 30:
            minute_30.append(subject_H[index])
STDV_minute_0 = np.std(minute_0)
STDV_minute_1 = np.std(minute_1)
STDV_minute_2 = np.std(minute_2)
STDV_minute_3 = np.std(minute_3)
STDV_minute_4 = np.std(minute_4)
STDV_minute_12 = np.std(minute_12)
STDV_minute_18 = np.std(minute_18)
STDV_minute_24 = np.std(minute_24)
STDV_minute_30 = np.std(minute_30)

all_av = [np.average(minute_0), np.average(minute_1), np.average(minute_2), np.average(minute_3), np.average(minute_4),
          np.average(minute_12), np.average(minute_18), np.average(minute_24), np.average(minute_30)]

# Create an error bar for each dataset
line_subject_A = ax.errorbar(0, np.average(minute_0), yerr=STDV_minute_0, **lineStyle_subject, color=color_subject_A, label='minute_0')
line_subject_B = ax.errorbar(1, np.average(minute_1), yerr=STDV_minute_1, **lineStyle_subject, color=color_subject_B, label='minute_1')
line_subject_C = ax.errorbar(2, np.average(minute_2), yerr=STDV_minute_2, **lineStyle_subject, color=color_subject_C, label='minute_2')
line_subject_D = ax.errorbar(3, np.average(minute_3), yerr=STDV_minute_3, **lineStyle_subject, color=color_subject_D, label='minute_3')
line_subject_E = ax.errorbar(4, np.average(minute_4), yerr=STDV_minute_4, **lineStyle_subject, color=color_subject_E, label='minute_4')
line_subject_F = ax.errorbar(12, np.average(minute_12), yerr=STDV_minute_12, **lineStyle_subject, color=color_subject_F, label='minute_12')
line_subject_G = ax.errorbar(18, np.average(minute_18), yerr=STDV_minute_18, **lineStyle_subject, color=color_subject_G, label='minute_18')
line_subject_H = ax.errorbar(24, np.average(minute_24), yerr=STDV_minute_24, **lineStyle_subject, color=color_subject_H, label='minute_24')
line_subject_k = ax.errorbar(30, np.average(minute_30), yerr=STDV_minute_30, **lineStyle_subject, color=color_subject_k, label='minute_30')

# plt.plot(axis, all_av,  "ro-")


# Draw a legend bar
plt.legend(handles=[line_subject_A, line_subject_B, line_subject_C, line_subject_D, line_subject_E, line_subject_F,
                    line_subject_G, line_subject_k], loc='upper right')


# perform the fit using the function where B is 0
def exponential(x, a, k, b):
    return a*np.exp(x*k) + b


popt_exponential, pcov_exponential = scipy.optimize.curve_fit(exponential, axis, all_av, p0=[1,-0.5, 1])


# Generate some data, you don't have to do this, as you already have your data
xdata = np.linspace(0, 30, 100)

ydata = all_av

# Plot the actual data


# Use the optimized parameters to plot the best fit
plt.plot(xdata, exponential(xdata, *popt_exponential), label="fit");


# Customize the tickes on the graph
plt.xticks(np.arange(0, 40, 1))
# plt.yticks(np.arange(100, 290, 5))

# Customize the legend font and handle length
params = {'legend.fontsize': 13,
          'legend.handlelength': 2}
plt.rcParams.update(params)

# Customize the font
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 12}
# Draw a grid for the graph
ax.grid(color='lightgrey', linestyle='-')
ax.set_facecolor('w')
plt.show()
=======
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize
from scipy.optimize import curve_fit
def normalize_data(data):
    return data / np.average(data)


subject_A = [253.61, 224.97, 219.55, 209.49, 188.4, 180.28, 195.29, 190.75, 194.8, 197.96, 193.61, 193.28, 193.16, 180.28, 198.31, 182.99]
axis_A = [0, 1, 1.25, 2, 3, 5, 6, 7, 8, 12, 13, 18, 19, 24, 25, 30]
subject_B = [161.31, 157.85, 166.18, 150.34, 145.33, 146.99, 145.03]
axis_B = [0, 1, 2, 12, 18, 24, 30]
subject_C = [198.99, 198.31, 192.91, 190.99, 194.83, 190.53, 185.59, 178.86, 187.27, 170.33, 168.09, 151.4]
axis_C = [0, 1, 2, 3, 4, 12, 18, 19, 24, 25, 30, 31]
subject_D = [271.41, 268.06, 268.34, 269.33, 266.81, 264.01, 261.83, 258.82, 254.76, 254.44, 252.53, 254.61, 248.72, 251.67, 252.55]
axis_D = [0, 1, 2.52, 3, 4, 5, 6, 7, 8, 12, 18, 19, 22, 24, 30]
subject_E = [155.85, 152.72, 153.36, 134.12, 131.59, 130.25, 127.84]
axis_E = [0, 1, 2, 12, 18, 24, 30]
subject_F = [181.99, 185.18, 177.21, 179.87, 158.16, 165.9, 159.14, 164.1]
axis_F = [0, 1, 2, 3, 4, 11, 12, 18]
subject_G = [196.56, 195.24, 189.99, 182.57, 182.35, 175.75, 136.88, 148.32, 149.93, 140.87, 131.98]
axis_G = [0, 1, 2, 3, 4, 5, 11, 16, 22, 28, 29]
subject_H = [199.92, 189.58, 196.72, 192.04, 182.8, 186.6, 189.96, 185.79]
axis_H = [0, 1, 2, 12, 18, 24, 30, 31]

subject_A = normalize_data(subject_A)
subject_B = normalize_data(subject_B)
subject_C = normalize_data(subject_C)
subject_D = normalize_data(subject_D)
subject_E = normalize_data(subject_E)
subject_F = normalize_data(subject_F)
subject_G = normalize_data(subject_G)
subject_H = normalize_data(subject_H)


# Create a figure with customized size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the axis lables
ax.set_xlabel('Time(min)', fontsize=18)
ax.set_ylabel('Haemoglobin Oxygenation (a.u.)', fontsize=18)


# Line color for error bar
color_subject_A = 'red'
color_subject_B = 'darkgreen'
color_subject_C = 'black'
color_subject_D = 'grey'
color_subject_E = 'blue'
color_subject_F = 'purple'
color_subject_G = 'brown'
color_subject_H = 'orange'
color_subject_k = 'blue'

# Line style for each dataset
lineStyle_subject = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}
minute_0 = []
minute_1 = []
minute_2 = []
minute_3 = []
minute_4 = []
minute_12 = []
minute_18 = []
minute_24 = []
minute_30 = []

axis = [0, 1, 2, 3, 4, 12, 18, 24, 30]
for i in axis:
    if i in axis_A:
        index = axis_A.index(i)
        if i == 0:
            minute_0.append(subject_A[index])
        if i == 1:
            minute_1.append(subject_A[index])
        if i == 2:
            minute_2.append(subject_A[index])
        if i == 3:
            minute_3.append(subject_A[index])
        if i == 4:
            minute_4.append(subject_A[index])
        if i == 12:
            minute_12.append(subject_A[index])
        if i == 18:
            minute_18.append(subject_A[index])
        if i == 24:
            minute_24.append(subject_A[index])
        if i == 30:
            minute_30.append(subject_A[index])
for i in axis:
    if i in axis_B:
        index = axis_B.index(i)
        if i == 0:
            minute_0.append(subject_B[index])
        if i == 1:
            minute_1.append(subject_B[index])
        if i == 2:
            minute_2.append(subject_B[index])
        if i == 3:
            minute_3.append(subject_B[index])
        if i == 4:
            minute_4.append(subject_B[index])
        if i == 12:
            minute_12.append(subject_B[index])
        if i == 18:
            minute_18.append(subject_B[index])
        if i == 24:
            minute_24.append(subject_B[index])
        if i == 30:
            minute_30.append(subject_B[index])
for i in axis:
    if i in axis_C:
        index = axis_C.index(i)
        if i == 0:
            minute_0.append(subject_C[index])
        if i == 1:
            minute_1.append(subject_C[index])
        if i == 2:
            minute_2.append(subject_C[index])
        if i == 3:
            minute_3.append(subject_C[index])
        if i == 4:
            minute_4.append(subject_C[index])
        if i == 12:
            minute_12.append(subject_C[index])
        if i == 18:
            minute_18.append(subject_C[index])
        if i == 24:
            minute_24.append(subject_C[index])
        if i == 30:
            minute_30.append(subject_C[index])
for i in axis:
    if i in axis_D:
        index = axis_D.index(i)
        if i == 0:
            minute_0.append(subject_D[index])
        if i == 1:
            minute_1.append(subject_D[index])
        if i == 2:
            minute_2.append(subject_D[index])
        if i == 3:
            minute_3.append(subject_D[index])
        if i == 4:
            minute_4.append(subject_D[index])
        if i == 12:
            minute_12.append(subject_D[index])
        if i == 18:
            minute_18.append(subject_D[index])
        if i == 24:
            minute_24.append(subject_D[index])
        if i == 30:
            minute_30.append(subject_D[index])
for i in axis:
    if i in axis_E:
        index = axis_E.index(i)
        if i == 0:
            minute_0.append(subject_E[index])
        if i == 1:
            minute_1.append(subject_E[index])
        if i == 2:
            minute_2.append(subject_E[index])
        if i == 3:
            minute_3.append(subject_E[index])
        if i == 4:
            minute_4.append(subject_E[index])
        if i == 12:
            minute_12.append(subject_E[index])
        if i == 18:
            minute_18.append(subject_E[index])
        if i == 24:
            minute_24.append(subject_E[index])
        if i == 30:
            minute_30.append(subject_E[index])
for i in axis:
    if i in axis_F:
        index = axis_F.index(i)
        if i == 0:
            minute_0.append(subject_F[index])
        if i == 1:
            minute_1.append(subject_F[index])
        if i == 2:
            minute_2.append(subject_F[index])
        if i == 3:
            minute_3.append(subject_F[index])
        if i == 4:
            minute_4.append(subject_F[index])
        if i == 12:
            minute_12.append(subject_F[index])
        if i == 18:
            minute_18.append(subject_F[index])
        if i == 24:
            minute_24.append(subject_F[index])
        if i == 30:
            minute_30.append(subject_F[index])
for i in axis:
    if i in axis_G:
        index = axis_G.index(i)
        if i == 0:
            minute_0.append(subject_G[index])
        if i == 1:
            minute_1.append(subject_G[index])
        if i == 2:
            minute_2.append(subject_G[index])
        if i == 3:
            minute_3.append(subject_G[index])
        if i == 4:
            minute_4.append(subject_G[index])
        if i == 12:
            minute_12.append(subject_G[index])
        if i == 18:
            minute_18.append(subject_G[index])
        if i == 24:
            minute_24.append(subject_G[index])
        if i == 30:
            minute_30.append(subject_G[index])
for i in axis:
    if i in axis_H:
        index = axis_H.index(i)
        if i == 0:
            minute_0.append(subject_H[index])
        if i == 1:
            minute_1.append(subject_H[index])
        if i == 2:
            minute_2.append(subject_H[index])
        if i == 3:
            minute_3.append(subject_H[index])
        if i == 4:
            minute_4.append(subject_H[index])
        if i == 12:
            minute_12.append(subject_H[index])
        if i == 18:
            minute_18.append(subject_H[index])
        if i == 24:
            minute_24.append(subject_H[index])
        if i == 30:
            minute_30.append(subject_H[index])
STDV_minute_0 = np.std(minute_0)
STDV_minute_1 = np.std(minute_1)
STDV_minute_2 = np.std(minute_2)
STDV_minute_3 = np.std(minute_3)
STDV_minute_4 = np.std(minute_4)
STDV_minute_12 = np.std(minute_12)
STDV_minute_18 = np.std(minute_18)
STDV_minute_24 = np.std(minute_24)
STDV_minute_30 = np.std(minute_30)

all_av = [np.average(minute_0), np.average(minute_1), np.average(minute_2), np.average(minute_3), np.average(minute_4),
          np.average(minute_12), np.average(minute_18), np.average(minute_24), np.average(minute_30)]

# Create an error bar for each dataset
line_subject_A = ax.errorbar(0, np.average(minute_0), yerr=STDV_minute_0, **lineStyle_subject, color=color_subject_A, label='minute_0')
line_subject_B = ax.errorbar(1, np.average(minute_1), yerr=STDV_minute_1, **lineStyle_subject, color=color_subject_B, label='minute_1')
line_subject_C = ax.errorbar(2, np.average(minute_2), yerr=STDV_minute_2, **lineStyle_subject, color=color_subject_C, label='minute_2')
line_subject_D = ax.errorbar(3, np.average(minute_3), yerr=STDV_minute_3, **lineStyle_subject, color=color_subject_D, label='minute_3')
line_subject_E = ax.errorbar(4, np.average(minute_4), yerr=STDV_minute_4, **lineStyle_subject, color=color_subject_E, label='minute_4')
line_subject_F = ax.errorbar(12, np.average(minute_12), yerr=STDV_minute_12, **lineStyle_subject, color=color_subject_F, label='minute_12')
line_subject_G = ax.errorbar(18, np.average(minute_18), yerr=STDV_minute_18, **lineStyle_subject, color=color_subject_G, label='minute_18')
line_subject_H = ax.errorbar(24, np.average(minute_24), yerr=STDV_minute_24, **lineStyle_subject, color=color_subject_H, label='minute_24')
line_subject_k = ax.errorbar(30, np.average(minute_30), yerr=STDV_minute_30, **lineStyle_subject, color=color_subject_k, label='minute_30')

# plt.plot(axis, all_av,  "ro-")


# Draw a legend bar
plt.legend(handles=[line_subject_A, line_subject_B, line_subject_C, line_subject_D, line_subject_E, line_subject_F,
                    line_subject_G, line_subject_k], loc='upper right')


# perform the fit using the function where B is 0
def exponential(x, a, k, b):
    return a*np.exp(x*k) + b


popt_exponential, pcov_exponential = scipy.optimize.curve_fit(exponential, axis, all_av, p0=[1,-0.5, 1])


# Generate some data, you don't have to do this, as you already have your data
xdata = np.linspace(0, 30, 100)

ydata = all_av

# Plot the actual data


# Use the optimized parameters to plot the best fit
plt.plot(xdata, exponential(xdata, *popt_exponential), label="fit");


# Customize the tickes on the graph
plt.xticks(np.arange(0, 40, 1))
# plt.yticks(np.arange(100, 290, 5))

# Customize the legend font and handle length
params = {'legend.fontsize': 13,
          'legend.handlelength': 2}
plt.rcParams.update(params)

# Customize the font
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 12}
# Draw a grid for the graph
ax.grid(color='lightgrey', linestyle='-')
ax.set_facecolor('w')
plt.show()
>>>>>>> 5f76680e (Initial commit)
