#test time to take old list of squares and change each r,g,b value at 680 x 480 dim

import time
newlist = []

start = time.process_time()
for i in range(1000000):
    x = (1 + i)
    newlist.append(x)
print(time.process_time() - start)