#!/bin/python3

import sys

def countInversions(arr):
    # Complete this function
    result = 0
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        res1 = countInversions(left_arr)
        res2 = countInversions(right_arr)
        
        i=0 # left_index
        j=0 # right_index
        k=0 # index of overall index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[j]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
                result = result + 1
            k=k+1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k +1
        result = result + res1 + res2
    #print(arr)
    return result

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
