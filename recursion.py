""" Recursion by Example """


def solution(seq, i=0):
  """ Returns a solution to a subproblem """
  if i == len(seq): return 0
  return solution(seq, i+1) + seq[i]

def testSolution(seq, i=0):
  """ Returns cost of our solution """
  if i == len(seq): return 1
  return testSolution(seq, i+1) + 1
