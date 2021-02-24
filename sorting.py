array2 = [63,4,12,423,423,6,57,57,8,523,53,74]
  
def bubble(array):
    swap = True
    while swap:
        swap = False
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i], array[i-1]= array[i-1],array[i]
                swap = True
    return array


def isSorted(array):
    if array == sorted(array):
        return True
        
def benchmark(n =[10,100,1000,10000]):
    from time import time
    b0 = []
    b1 = []
    for length in n:
        a = [23,4,234,234,2,62,789,7,4,975,74,531,31,63,8,5896,9]
        t0 = time()
        s= sorted(array)
        t1=  time()
        b1.append(t1-t0)
         
        t0 = time()
        s=bubble(array)
        t1 = time()
        b0.append(t1-t0)
    print("\tBuilt In\tBubble Sort")
    print("____________________________________")
    for i, cur_n in enumerate(n):
        print(cur_n, b1[i],b0[i])
        
    
array = bubble([63,4,12,423,423,6,57,57,8,523,53,74])
print(array2)
print(array)
arraySorted = isSorted(array)
print(arraySorted)

benchmark()

def selection(array):
    sorted_length = 0 
    while sorted_length < len(array):
        minimum_index = None
        for i,elem in enumerate(array[sorted_length:]):
            if minimum_index == None or elem < array[minimum_index]:
                minimum_index = i + sorted_length
        array[sorted_length], array[minimum_index] = array[minimum_index], array[sorted_length] 
        sorted_length = sorted_length + 1
    return array
    
a2 = selection([63,4,12,423,423,6,57,57,8,523,53,74])

print(a2)
        

def selection2(array):
    index_len = range(0, len(array) -1 )
    for i in index_len:
        min_val = i
        for j in range(i+1 , len(array)):
            if array[j] < array[min_val]:
                min_val = j
        if min_val != i:
            array[min_val], array[i] = array[i], array[min_val]
    return array
    
    
a3 = selection2([6,5,3,68,8,23,4,54,534])

print(a3)
    

def insertion(a):
    for i in range(1, len(a)):
        next_unsorted = a[i]
        insert_index = i
        
        while insert_index > 0 and next_unsorted < a[insert_index -1]:
            a[insert_index] = a[insert_index-1]
            insert_index +=-1
        a[insert_index] = next_unsorted
    return a
            
        
a4 = insertion([1,5,3,5,25,346,34])

print(a4)
def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [4,4,5,2,1,3,6,7,7,9,6,5,423,423,5,235,23,523,765,889,6,978,31,4,16,4,86]
mergeSort(nlist)
print(nlist)


def quicksort(a):
    if len(a)<=1:
        return a
    pivot = a.pop()
    smaller = []
    larger = []
    equal = []
    
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort(smaller) + [pivot] + quicksort(equal) + quicksort(larger)
a2 = quicksort([1,3,5,5,5,5,5,5,7,3,5,8,4])
print(a2)
