# bubble sor

# selection sort

def selection_sert():
    for step in range(len(array)):
        min_index = step

        for i in range(step+1, len(array)):
            if array[i]<array[min_index]:
                min_index = i
        array[min_index], array[i] = array[i], array[min_index]


# insertion sort
# data = [9, 5, 1, 4, 3]
                
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step-1

        while j>=0 and key < array[j]:
            array[j+1]=array[j]
            j = j-1
        array[j+1]=key
