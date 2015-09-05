#遇到'('，怎在结果队列中添加0
#如果遇到')'则判断栈中是否有可用的'(',如果没有，则添加-1，否则去结果队列中最后的值加2
#然后合并队尾中的非0值
s = ')()(()()(()))'
max = 0
i = 0
st = 0
a =[]
esp = -1

for i in range(len(s)):
	if (s[i] == '('):
		a.append(0)
		esp += 1
		st += 1
	elif ((s[i] == ')') & (st > 0)):
		st -= 1
		if (a[esp] == 0):
			a[esp] = 2
		elif ((esp > 0) and (a[esp] >= 0)):
			a[esp - 1] = a[esp] + 2
			a.pop()
			esp -= 1
		else:
			print 'error'
			
		if ((esp > 0) and (a[esp - 1]>0)):
			a[esp-1] += a[esp]
			a.pop()
			esp -= 1
	else:
		a.append(-1)
		esp += 1

print a, len(a)
for i in a:
	if (i > max):
		max = i
	
print max