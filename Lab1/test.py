import urllib.request
import time

times = []

for i in range(100):
    start = time.time()
    urllib.request.urlopen('http://127.0.0.1:5000/')
    end = time.time()
    times.append(end - start)
    print(f'Request {i+1}: {times[-1]:.3f}s')

s = sorted(times)
print('')
print('Min:', round(min(times), 3))
print('Max:', round(max(times), 3))
print('Avg:', round(sum(times)/len(times), 3))
print('P50:', round(s[49], 3))
print('P90:', round(s[89], 3))
print('P99:', round(s[98], 3))