
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
for i in range(len(num2)-len(num1)+1):
	for j in range(len(num1)):
		if num1[j] != num2[i+j]:
			print ('Not')
			break
	else:
			print ('subset')