import numpy as np
def maxtrix_of_MN(m, n):
  odd_matrix = (np.arange(m*n)*2 + 1).reshape(m, n)
  return np.where(odd_matrix % 3 == 0, 0, odd_matrix)
m = int(input())
n = int(input())
maxtrix_of_MN(m, n)