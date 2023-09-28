import time
import sys
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

dataType = 2
data = [5, 4, 7, 6, 3, 2, 1, 8, 9, 6, 0, 1]
databubble = datamerge = dataquick = datainsertion = data
sys.setrecursionlimit(5000)

def routerSmall(event):
    updateSmall()

def routerMedium(event):
    updateMedium()

def routerLarge(event):
    updateLarge()

def routerHuge(event):
    updateHuge()

def updateSmall():
    data = []
    for i in range(12):
        data.append(random.randint(0, 4500))
    updateData(data)

def updateMedium():
    data = []
    for i in range(1000):
        data.append(random.randint(0, 4500))
    updateData(data)

def updateLarge():
    data = []
    for i in range(10_000):
        data.append(random.randint(0, 4500))
    updateData(data)

def updateHuge():
    data = []
    for i in range(100_000):
        data.append(random.randint(0, 4500))
    updateData(data)

def updateData(data):
    plt.close()

    global databubble, datamerge, dataquick, datainsertion, x, y

    databubble = datamerge = dataquick = datainsertion = data

    bubbleStart = time.time()
    bubble_sort(databubble)
    bubbleProcess = time.time() - bubbleStart

    quickStart = time.time()
    quick_sort(dataquick)
    quickProcess = time.time() - quickStart

    insertionStart = time.time()
    insertion_sort(datainsertion)
    insertionProcess = time.time() - insertionStart

    mergeStart = time.time()
    merge_sort(datamerge)
    mergeProcess = time.time() - mergeStart

    y = [bubbleProcess, quickProcess, insertionProcess, mergeProcess]

    fig, ax = plt.subplots()
    line, = ax.plot(x, y)
    ax.set_xlabel('Kinds Of Sorting Methods')
    ax.set_ylabel('Working Times')


    ax_button = plt.axes([0.51, 0.9, 0.09, 0.06])
    buttonS = Button(ax_button, 'Small', hovercolor='0.9')
    buttonS.on_clicked(routerSmall)

    ax_button = plt.axes([0.61, 0.9, 0.09, 0.06])
    buttonM = Button(ax_button, 'Medium', hovercolor='0.9')
    buttonM.on_clicked(routerMedium)

    ax_button = plt.axes([0.71, 0.9, 0.09, 0.06])
    buttonL = Button(ax_button, 'Large', hovercolor='0.9')
    buttonL.on_clicked(routerLarge)

    ax_button = plt.axes([0.81, 0.9, 0.09, 0.06])
    buttonH = Button(ax_button, 'Huge', hovercolor='0.9')
    buttonH.on_clicked(routerHuge)
    
    if(len(data) == 12):
        plt.text(-9, 0, 'Length: 12')
    if(len(data) == 1_000):
        plt.text(-9, 0, 'Length: 1.000')
    if(len(data) == 10_000):
        plt.text(-9, 0, 'Length: 10.000')
    if(len(data) == 100_000):
        plt.text(-9, 0, 'Length: 100.000')
    processes = [bubbleProcess,quickProcess,insertionProcess,mergeProcess]
    smallestProcess = min(processes)
    processes.remove(smallestProcess)
    secondSmallestProcess = min(processes)
    if(smallestProcess == bubbleProcess):
        smallestProcess = 'Best is Bubble: ' + str(bubbleProcess)
    if(smallestProcess == quickProcess):
        smallestProcess = 'Best is Quick: ' + str(quickProcess)
    if(smallestProcess == insertionProcess):
        smallestProcess = 'Best is Insertion: ' + str(insertionProcess)
    if(smallestProcess == mergeProcess):
        smallestProcess = 'Best is Merge: ' + str(mergeProcess)

    if(secondSmallestProcess == bubbleProcess):
        secondSmallestProcess = 'Second is Bubble: ' + str(bubbleProcess)
    if(secondSmallestProcess == quickProcess):
        secondSmallestProcess = 'Second is Quick: ' + str(quickProcess)
    if(secondSmallestProcess == insertionProcess):
        secondSmallestProcess = 'Second is Insertion: ' + str(insertionProcess)
    if(secondSmallestProcess == mergeProcess):
        secondSmallestProcess = 'Second is Merge: ' + str(mergeProcess)   

    plt.text(-9, 1, smallestProcess)
    plt.text(-9, 0.5, secondSmallestProcess)
    plt.show()


def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[int(len(arr)/2)]
        less = []
        for x in arr[1:]:
            if x <= pivot:
                less.append(x)
        higher = []
        for x in arr[1:]:
            if x > pivot:
                higher.append(x)
        return quick_sort(less) + [pivot] + quick_sort(higher)

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
        merge_sort(sub_array1)
        merge_sort(sub_array2)
        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
    return arr

bubbleStart = time.time()
bubble_sort(databubble)
bubbleProcess = time.time() - bubbleStart

quickStart = time.time()
quick_sort(dataquick)
quickProcess = time.time() - quickStart

insertionStart = time.time()
insertion_sort(datainsertion)
insertionProcess = time.time() - insertionStart

mergeStart = time.time()
merge_sort(datamerge)
mergeProcess = time.time() - mergeStart

x = ['BubbleSort', 'QuickSort', 'InsertionSort', 'MergeSort']
y = [bubbleProcess, quickProcess, insertionProcess, mergeProcess]

fig, ax = plt.subplots()
line, = ax.plot(x, y)
ax.set_xlabel('Kinds Of Sorting Methods')
ax.set_ylabel('Working Times')

# Butonu oluşturun
ax_button = plt.axes([0.51, 0.9, 0.09, 0.06])
buttonS = Button(ax_button, 'Small', hovercolor='0.9')
buttonS.on_clicked(routerSmall)

ax_button = plt.axes([0.61, 0.9, 0.09, 0.06])
buttonM = Button(ax_button, 'Medium', hovercolor='0.9')
buttonM.on_clicked(routerMedium)

ax_button = plt.axes([0.71, 0.9, 0.09, 0.06])
buttonL = Button(ax_button, 'Large', hovercolor='0.9')
buttonL.on_clicked(routerLarge)

ax_button = plt.axes([0.81, 0.9, 0.09, 0.06])
buttonH = Button(ax_button, 'Huge', hovercolor='0.9')
buttonH.on_clicked(routerHuge)

# Grafiği gösterin
plt.show()
