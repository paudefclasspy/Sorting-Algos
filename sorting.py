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
    
        
