import ctypes
nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
times = []
for i in range(0, 32):
	times.append(0)

for i in nums:
	t = 1
	for j in range(0, 32):
		if (i & t):
			times[j] += 1
		t = t << 1

ans = 0        
for i in range(0, 32):
	if (times[i] % 3 != 0):
		ans = ans + (1 << i)
		
print ctypes.c_int32(ans).value