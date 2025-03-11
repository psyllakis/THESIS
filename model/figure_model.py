<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# First dataset
"""def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))"""


def normalize_data(data):
    return (data / np.average(data))


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



"""print(subject_A)
print(subject_B)
print(subject_C)
print(subject_D)
print(subject_F)
print(subject_G)
print(subject_H)"""

# Caluclate the standard deviation of datasets
STDV_subject_A = np.std(subject_A)
STDV_subject_B = np.std(subject_B)
STDV_subject_C = np.std(subject_C)
STDV_subject_D = np.std(subject_D)
STDV_subject_E = np.std(subject_E)
STDV_subject_F = np.std(subject_F)
STDV_subject_G = np.std(subject_G)
STDV_subject_H = np.std(subject_H)

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

# Line style for each dataset
lineStyle_subject = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}


# Create an error bar for each dataset
line_subject_A = ax.errorbar(axis_A, subject_A, yerr=STDV_subject_A, **lineStyle_subject, color=color_subject_A, label='subject A')
line_subject_B = ax.errorbar(axis_B, subject_B, yerr=STDV_subject_B, **lineStyle_subject, color=color_subject_B, label='subject B')
line_subject_C = ax.errorbar(axis_C, subject_C, yerr=STDV_subject_C, **lineStyle_subject, color=color_subject_C, label='subject C')
line_subject_D = ax.errorbar(axis_D, subject_D, yerr=STDV_subject_D, **lineStyle_subject, color=color_subject_D, label='subject D')
line_subject_E = ax.errorbar(axis_E, subject_E, yerr=STDV_subject_E, **lineStyle_subject, color=color_subject_E, label='subject E')
line_subject_F = ax.errorbar(axis_F, subject_F, yerr=STDV_subject_F, **lineStyle_subject, color=color_subject_F, label='subject F')
line_subject_G = ax.errorbar(axis_G, subject_G, yerr=STDV_subject_G, **lineStyle_subject, color=color_subject_G, label='subject G')
line_subject_H = ax.errorbar(axis_H, subject_H, yerr=STDV_subject_H, **lineStyle_subject, color=color_subject_H, label='subject H')


"""# Label each dataset on the graph, xytext is the label's position
for i, txt in enumerate(subject_A):
    ax.annotate(txt, xy=(axis_A[i], subject_A[i]), color=color_subject_A)
for i, txt in enumerate(subject_B):
    ax.annotate(txt, xy=(axis_B[i], subject_B[i]), xytext=(axis_B[i] + 0.03, subject_B[i] + 0.3), color=color_subject_B)
for i, txt in enumerate(subject_C):
    ax.annotate(txt, xy=(axis_C[i], subject_C[i]), xytext=(axis_C[i] + 0.03, subject_C[i] + 0.3), color=color_subject_C)
for i, txt in enumerate(subject_D):
    ax.annotate(txt, xy=(axis_D[i], subject_D[i]), xytext=(axis_D[i] + 0.03, subject_D[i] + 0.3), color=color_subject_D)
for i, txt in enumerate(subject_E):
    ax.annotate(txt, xy=(axis_E[i], subject_E[i]), xytext=(axis_E[i] + 0.03, subject_E[i] + 0.3), color=color_subject_E)
for i, txt in enumerate(subject_F):
    ax.annotate(txt, xy=(axis_F[i], subject_F[i]), xytext=(axis_F[i] + 0.03, subject_F[i] + 0.3), color=color_subject_F)
for i, txt in enumerate(subject_G):
    ax.annotate(txt, xy=(axis_G[i], subject_G[i]), xytext=(axis_G[i] + 0.03, subject_G[i] + 0.3), color=color_subject_G)
for i, txt in enumerate(subject_H):
    ax.annotate(txt, xy=(axis_H[i], subject_H[i]), xytext=(axis_H[i] + 0.03, subject_H[i] + 0.3), color=color_subject_H)
"""

# Draw a legend bar
plt.legend(handles=[line_subject_A, line_subject_B, line_subject_C, line_subject_D, line_subject_E, line_subject_F,
                    line_subject_G], loc='upper right')


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
import numpy as np
import pandas as pd


# First dataset
"""def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))"""


def normalize_data(data):
    return (data / np.average(data))


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



"""print(subject_A)
print(subject_B)
print(subject_C)
print(subject_D)
print(subject_F)
print(subject_G)
print(subject_H)"""

# Caluclate the standard deviation of datasets
STDV_subject_A = np.std(subject_A)
STDV_subject_B = np.std(subject_B)
STDV_subject_C = np.std(subject_C)
STDV_subject_D = np.std(subject_D)
STDV_subject_E = np.std(subject_E)
STDV_subject_F = np.std(subject_F)
STDV_subject_G = np.std(subject_G)
STDV_subject_H = np.std(subject_H)

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

# Line style for each dataset
lineStyle_subject = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}


# Create an error bar for each dataset
line_subject_A = ax.errorbar(axis_A, subject_A, yerr=STDV_subject_A, **lineStyle_subject, color=color_subject_A, label='subject A')
line_subject_B = ax.errorbar(axis_B, subject_B, yerr=STDV_subject_B, **lineStyle_subject, color=color_subject_B, label='subject B')
line_subject_C = ax.errorbar(axis_C, subject_C, yerr=STDV_subject_C, **lineStyle_subject, color=color_subject_C, label='subject C')
line_subject_D = ax.errorbar(axis_D, subject_D, yerr=STDV_subject_D, **lineStyle_subject, color=color_subject_D, label='subject D')
line_subject_E = ax.errorbar(axis_E, subject_E, yerr=STDV_subject_E, **lineStyle_subject, color=color_subject_E, label='subject E')
line_subject_F = ax.errorbar(axis_F, subject_F, yerr=STDV_subject_F, **lineStyle_subject, color=color_subject_F, label='subject F')
line_subject_G = ax.errorbar(axis_G, subject_G, yerr=STDV_subject_G, **lineStyle_subject, color=color_subject_G, label='subject G')
line_subject_H = ax.errorbar(axis_H, subject_H, yerr=STDV_subject_H, **lineStyle_subject, color=color_subject_H, label='subject H')


"""# Label each dataset on the graph, xytext is the label's position
for i, txt in enumerate(subject_A):
    ax.annotate(txt, xy=(axis_A[i], subject_A[i]), color=color_subject_A)
for i, txt in enumerate(subject_B):
    ax.annotate(txt, xy=(axis_B[i], subject_B[i]), xytext=(axis_B[i] + 0.03, subject_B[i] + 0.3), color=color_subject_B)
for i, txt in enumerate(subject_C):
    ax.annotate(txt, xy=(axis_C[i], subject_C[i]), xytext=(axis_C[i] + 0.03, subject_C[i] + 0.3), color=color_subject_C)
for i, txt in enumerate(subject_D):
    ax.annotate(txt, xy=(axis_D[i], subject_D[i]), xytext=(axis_D[i] + 0.03, subject_D[i] + 0.3), color=color_subject_D)
for i, txt in enumerate(subject_E):
    ax.annotate(txt, xy=(axis_E[i], subject_E[i]), xytext=(axis_E[i] + 0.03, subject_E[i] + 0.3), color=color_subject_E)
for i, txt in enumerate(subject_F):
    ax.annotate(txt, xy=(axis_F[i], subject_F[i]), xytext=(axis_F[i] + 0.03, subject_F[i] + 0.3), color=color_subject_F)
for i, txt in enumerate(subject_G):
    ax.annotate(txt, xy=(axis_G[i], subject_G[i]), xytext=(axis_G[i] + 0.03, subject_G[i] + 0.3), color=color_subject_G)
for i, txt in enumerate(subject_H):
    ax.annotate(txt, xy=(axis_H[i], subject_H[i]), xytext=(axis_H[i] + 0.03, subject_H[i] + 0.3), color=color_subject_H)
"""

# Draw a legend bar
plt.legend(handles=[line_subject_A, line_subject_B, line_subject_C, line_subject_D, line_subject_E, line_subject_F,
                    line_subject_G], loc='upper right')


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
