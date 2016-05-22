""" Examples of Sorting Algorithms using python """

def gnomesort(seq):
    """ Gnome Sort """
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

def mergesort(seq):
    """ Merge Sort """
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(rgt.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


def ins_sort_rec(seq, i):
    """ Recursive Insertion Sort """
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


def ins_sort(seq):
    """ Insertion Sort """
    for i in range(1, len(seq)):                    # 0..i-1 sorted so far
        j = i                                       # Start walking down
        while j > 0 and seq[j-1] > seq[j]:          # Look for OK spot
            seq[j-1], seq[j] = seq[j], seq[j-1]     # Keep moving seq[j] down
            j -= 1                                  # Decrement j


def sel_sort_rec(seq, i):
    """ Recursive Selection Sort """
    if i == 0: return
    max_j = i                                       # idx of lrgest val so far
    for j in range(i):                              # Look for larger val
        if seq[j] > seq[max_j]:                     # Found one? Update max_j
            max_j = j
            seq[i], seq[max_j] = seq[max_j], seq[i] # Switch lrgest into place
            sel_sort_rec(seq, i-1)                  # Sort 0..i-1


def sel_sort(seq):
    """ Selection Sort """
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]


def naive_max_perm(M, A=None):
    """ INEFFICIENT Naive Implementation of the Recursive Algoright For Finding
    Maximum Permutation """
    if A is None:
        A = set(range(len(M)))                      # A = {0, 1, ... , n-1}
    if len(A) == 1:
      return A                                      # Base Case
    B = set(M[i] for i in A)                        # The "pointed to" elements
    C = A -B                                        # NOT "pointed to" elements
    if C:                                           # Any useless elements?
      A.remove(C.pop())                             # Remove one of them
      return naive_max_perm(M, A)                   # Solve remaining problem
    return A                                        # All useful -- return all


def max_perm(M):
    """ Finding a Maximum Permutation """
    n = len(M)                                        # How many elements?
    A = set(range(n))                                 # A = {0, 1, ..., n-1}
    count = [0] * n                                   # C[i] == 0 for i in A
    for i in M:                                       # All that are "pointed to"
        count[i] += 1                                 # Increment "point count"
    O = [i for i in A if count[i] == 0]               # Useless elements
    while O:                                          # While useless elmts left...
         i = O.pop()                                  # Get one
         A.remove(i)                                  # Remove it
         j = M[i]                                     # Who's it pointing to?
         count[j] -= 1                                # Not anymore ...
         if count[j] == 0:                            # Is j useless now?
            O.append(j)                               # Then deal w/it next
    return A                                          # Return useful elmts.


def naive_celeb(G):
    """ A Naive Solution to the Celebrity Problem """
    n = len(G)
    for u in range(n):                                # For every candidate...
        for v in range(n):                            # For everyone else...
            if u == v:
              continue                                # Same person? Skip.
            if G[u][v]:
              break                                   # Candidate knows other
            if not G[v][u]:
              break                                   # Other candidate doesn't know candidate
            else:
                return u                              # No breaks? Celebrity!
        return None                                   # Couldn't find anyone


from collections import defaultdict


def counting_sort(A, key=lambda x: x):
    """ Counting Sort """
    B, C = [], defaultdict(list)                      # Output and "counts"
    for x in A:
        C[key(x)].append(x)                           # "Count" key(x)
    for k in range(min(C), max(C) + 1):               # For every key in range
        B.extend(C[k])                                # Add values in sorted order
    return B
