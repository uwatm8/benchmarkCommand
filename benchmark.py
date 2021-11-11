import time
from time import process_time
import os
times=[]
totalTime=0
runs = 5
for i in range(runs): 
  s1 = time.time()
  os.popen("yarn clean && yarn build:legal").read()
  e1 = time.time()
  testTime = e1-s1
  times.append(testTime)
  totalTime = totalTime +testTime
  print("time: ", e1-s1)
print("times", times)
print("total time", totalTime)
print("avg time", totalTime/runs)

