import matplotlib.pyplot as plt

# gather data
work_left = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
time_remaining = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# plot data
plt.plot(time_remaining, work_left)

# add labels and format chart
plt.xlabel("Time Remaining")
plt.ylabel("Work Left")
plt.title("Burn Down Chart")

# display chart
plt.show()
