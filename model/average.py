import matplotlib.pyplot as plt
import numpy as np
import statistics


def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


minute_0 = [253, 161, 199, 271, 155, 181, 196, 199]
avg_0 = sum(minute_0)/len(minute_0)
print(avg_0)
print("Standard Deviation of the sample is % s "% (statistics.stdev(minute_0)))
print("Variance of the minute_0 is % s" %(statistics.variance(minute_0)))

minute_1 = [221, 157, 198, 268, 152, 185, 195, 189]
avg_1 = sum(minute_1)/len(minute_1)
print(avg_1)
print("Standard Deviation of the sample is % s "% (statistics.stdev(minute_1)))
print("Variance of the minute_1 is % s" %(statistics.variance(minute_1)))

minute_2 = [209, 192, 268, 177, 189, 196]
avg_2 = sum(minute_2)/len(minute_2)
print(avg_2)
print("Standard Deviation of the sample is % s "% (statistics.stdev(minute_2)))
print("Variance of the minute_2 is % s" %(statistics.variance(minute_2)))


minute_3 = [188, 191, 269, 179, 182]
avg_3 = sum(minute_3)/len(minute_3)
print(avg_3)
print("Standard Deviation of the sample is % s " % (statistics.stdev(minute_3)))
print("Variance of the minute_3 is % s" %(statistics.variance(minute_3)))


minute_4 = [195, 266, 158, 182]
avg_4 = sum(minute_4)/len(minute_4)
print(avg_4)
print("Standard Deviation of the sample is % s " % (statistics.stdev(minute_4)))
print("Variance of the minute_4 is % s" % (statistics.variance(minute_4)))

minute_12 = [197, 166, 190, 254, 153, 159, 136, 192]
avg_12 = sum(minute_12)/len(minute_12)
print(avg_12)
print("Standard Deviation of the minute_12 is % s " % (statistics.stdev(minute_12)))
print("Variance of the minute_12 is % s" % (statistics.variance(minute_12)))

minute_18 = [193, 150, 185, 252, 134, 164, 182]
avg_18 = sum(minute_18)/len(minute_18)
print(avg_18)
print("Standard Deviation of the minute_18 is % s " % (statistics.stdev(minute_18)))
print("Variance of the minute_18 is % s" %(statistics.variance(minute_18)))

minute_24 = [180, 146, 187, 251, 131, 186]
avg_24 = sum(minute_24)/len(minute_24)
print(avg_24)
print("Standard Deviation of the minute_24 is % s " % (statistics.stdev(minute_24)))
print("Variance of the minute_24 is % s" %(statistics.variance(minute_24)))

minute_30 = [182, 145, 168, 252, 127, 131, 189]
avg_30 = sum(minute_30)/len(minute_30)
print(avg_30)
print("Standard Deviation of the minute_30 is % s " % (statistics.stdev(minute_30)))
print("Variance of the minute_30 is % s" %(statistics.variance(minute_30)))

time = [0, 1, 2, 3, 4,  12, 18, 24, 30]
a = [avg_0, avg_1, avg_2, avg_3, avg_4, avg_12, avg_18, avg_24, avg_30]
plt.plot(time, a, "ro-")
plt.xlabel("Time (min)")
plt.xlim(-1, 40)
plt.ylabel("Haemoglobin Oxygenation (a.u.)")
# plt.text(15, 190, 'n:8', dict(size=20))
plt.title("Hemoglobin Oxygenation Dynamic Graph ")
plt.show()



