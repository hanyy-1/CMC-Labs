import matplotlib.pyplot as plt

times = [0.126,0.030,0.058,0.019,0.124,0.047,0.032,0.453,0.102,0.321,0.216,0.010,0.014,0.570,0.026,0.030,0.004,0.053,0.013,0.007,0.181,0.050,0.083,0.052,0.117,0.057,0.063,0.011,0.133,0.060,0.137,0.089,0.061,0.186,0.031,0.036,0.071,0.036,0.010,0.061,0.077,0.240,0.023,0.034,0.059,0.030,0.250,0.091,0.037,0.195,0.117,0.035,0.358,0.093,0.066,0.122,0.035,0.067,0.132,0.069,0.211,0.070,0.008,0.043,0.407,0.147,0.037,0.009,0.038,0.047,0.165,0.107,0.057,0.006,0.230,0.188,0.196,0.021,0.128,0.061,0.213,0.371,0.017,0.071,0.034,0.111,0.056,0.149,0.187,0.160,0.008,0.095,0.171,0.102,0.107,0.251,0.028,0.246,0.018,0.172]

plt.figure(figsize=(10,6))
plt.hist(times, bins=20, color='steelblue', edgecolor='black')
plt.axvline(x=0.067, color='green', linestyle='--', label='P50 = 0.067s')
plt.axvline(x=0.230, color='orange', linestyle='--', label='P90 = 0.230s')
plt.axvline(x=0.453, color='red', linestyle='--', label='P99 = 0.453s')
plt.xlabel('Response Time (seconds)')
plt.ylabel('Number of Requests')
plt.title('Tail Latency Histogram - 100 Requests to Flask App')
plt.legend()
plt.tight_layout()
plt.savefig('C:/lab1/histogram.png')
plt.show()
print('Histogram saved!')