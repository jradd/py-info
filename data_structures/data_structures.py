#!/usr/bin/env python

class MyList:
  def __init__(self, size=1):
    self.items = [None] * size
    self.numItems = 0

  def append(self, item):
    if self.numItems == len(self.items):
      newlst = [None] * self.numItems * 2
      for k in range(len(self.items)):
        newlst[k] = self.items[k]

        self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1

def main():
  p = MyList()

  for k in range(100):
    p.append(k)

    print(p.items)
    print(p.numItems)
    print(len(p.items))

if __name__ == "__main__":
  main()
