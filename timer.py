import time
dict = {}
for i in range(100000):
    dict[i] = 12
start = time.time()
if 10000000 in dict:
    print('baka')
else:
    print('youre a baka')
end = time.time()
print(end-start)