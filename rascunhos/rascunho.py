from random import *
from sortingAlgorithms import *
from time import time 
from matplotlib import pyplot as plt
import pandas as pd

def generateInputs(n:int)->dict:
    ordered = [i for i in range(n)]
    reverse = [n-i for i in range(n)]
    random = [randint(0,10*n) for _ in range(n)]
    return {'ordered':ordered,'reverse':reverse,'random':random}

algo_names = 'betterBubbleSort bubbleSort heapSort insertionSort mergeSort selectionSort shellSort'.split()
algorithms = {
    'betterBubbleSort':betterBubbleSort, 
    'bubbleSort':bubbleSort,
    'heapSort': heapSort,
    'insertionSort':insertionSort,
    'mergeSort':mergeSort,
    'selectionSort':selectionSort,
    'shellSort':shellSort
    }

number_of_elements = [1000, 2000, 3000, 4000, 5000, 7500, 10000, 15000, 20000, 30000, 40000, 50000]
times = {}
for number in number_of_elements:
    for name in algo_names:
            
        times[number] = {}
        inputs = generateInputs(number)
        for input_type in inputs:
            
            # Start timer
            start = time()
            
            # Run algorithm
            
            arr = algorithms[name](inputs[input_type])

            # Stop timer
            stop = time()

            elapsedTime = stop-start

            

            # Stores information if the list was correctly sorted
            if arr == sorted(arr):
                times[number][input_type] = elapsedTime
            else: raise Exception("The result is not ordered!")