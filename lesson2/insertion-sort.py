import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    insertionSort(arr)
    print(arr)