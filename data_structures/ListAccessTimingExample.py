#!/usr/bin/env python
import datetime
import random
import time

def main():
# Write results to XML file
  file = open("results.xml", "w")

  file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
  file.write('<Plot title="Avg List Element Access Time">\n')

# Constants to setup for the size of our list
# In this case we will use list size 1000 to 10000
  xmin = 1000
  xmax = 10000

# Record list sizes in xList and the avg access time with
# a list that size in yList for 1000 retrievals.
  xList = []
  yList = []

  for x in range(xmin, xmax+1, 1000):
    xList.append(x)

    prod = 0
# Creates a list of size x with all 0's
    lst = [0] * x

# Let's take a quick break to allow for garbage collection/memory-allocation
    time.sleep(1)

# Get the start time for the 1000 test retrievals
    start_t = datetime.datetime.now()

    for v in range(1000):
# Find random location within list and retrieve value.
# Perform a dummy operation to be sure it was retrieved.
      index = random.randint(0, x-1)
      val = lst[index]
      prod = prod * val
# Time after the 1000 test retrievals
      stop_t = datetime.datetime.now()

# Difference between stop/start time
      deltaT = stop_t - start_t

# Divide by 1000 for the avg access time
# multiply by 1000000 for microseconds
    accessTime = deltaT.total_seconds() * 1000

    yList.append(accessTime)

  file.write('  <Axes>\n')
  file.write('    <XAxis min="'+str(xmin) +'" max="'+str(xmax)+'">List Size</XAxis>\n')
  file.write('    <YAxis min="'+str(min(yList)) +'" max="'+str(60)+'">Micro Seconds</YAxis>\n')
  file.write('  </Axes>\n')

  file.write('  <Sequence title="Avg Access Time vs List Size" color="red">\n')

  for i in range(len(xList)):
    file.write('      <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')
  
  file.write('  </Sequence>\n')

# Test access at 100 random locations within a list of 200k elements for comparison
  xList = lst
  yList = [0] * 200000

  time.sleep(2)

  for i in range(100):
    start_t = datetime.datetime.now()
    index = random.randint(0, 200000-1)
    xList[index] = xList[index] + 1
    stop_t = datetime.datetime.now()
    deltaT = stop_t - start_t
    yList[index] = yList[index] + deltaT.total_seconds() * 1000000

  file.write('  <Sequence title="Access Time Distribution" color="blue">\n')

  for i in range(len(xList)):
    if xList[i] > 0:
      file.write('    <DataPoint x="'+str(i)+'" y="'+str(yList[i]/xList[i])+'"/>\n')

  file.write('  </Sequence>\n')
  file.write('</Plot>\n')
  file.close()

if __name__ == '__main__':
  main()
