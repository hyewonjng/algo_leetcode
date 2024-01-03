# bubble sort

data = [-2, 45, 0, 11, -9]

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            # if left is greater than right
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

bubbleSort(data)

# selection sort

def selection_sert():
    for step in range(len(array)):
        min_index = step

        for i in range(step+1, len(array)):
            if array[i]<array[min_index]:
                min_index = i
        array[min_index], array[i] = array[i], array[min_index]


# insertion sort
# https://www.programiz.com/dsa/insertion-sort
# data = [9, 5, 1, 4, 3]
                
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step-1

        while j>=0 and key < array[j]:
            array[j+1]=array[j]
            j = j-1
        array[j+1]=key

# MergeSort
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)