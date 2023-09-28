# SortExamples
The working speeds of 4 ranking algorithms on some data sets are compared.

First, I would like to briefly talk about what sorting algorithms are and what they are used for. Sorting algorithms are algorithms that allow us to align a data set on a linear line. Selection Sort, Quick Sort, Merge Sort, Heap Sort, Counting Sort, Bubble Sort, Insertion Sort, and more. We can increase the optimization of our application by using these algorithms after selecting them according to the size of the data set.

## Bubble Sort
We look at the data set 2 by 2, respectively, from the beginning. Then, after sorting each 2 from smallest to largest and swapping places, we repeat this process over and over again as many times as the number of data. In this way, our data is sorted.
<br>![bubblepass](https://github.com/furkancankay/SortExamples/assets/139324087/7da51292-794f-4673-82b5-8f61492fb6ed)<br>

The notation is O(n^2)

## Quick Sort
We select a number from the data set, which we call pivot. Then, we throw the ones larger than this pivot to the right and the ones smaller than this pivot to the right. We now have 2 lists. Now we assign these 2 lists to this function recursively. In this way, each fragmented list is sorted and fragmented. Finally, we have a sorted list.
<br>![partitionA](https://github.com/furkancankay/SortExamples/assets/139324087/569352f8-df34-4bae-a2c0-9008a60663c6)<br>
<br>![firstsplit](https://github.com/furkancankay/SortExamples/assets/139324087/f41ac7e0-c83b-4740-8e20-3fd549485b4a)<br>

The notation is O(n^2)

## Insertion Sort
We look at the first number and the next number. Whichever is smaller moves to the left. But this process of moving to the left continues until the one on the left is bigger than the one on the left.
<br>![insertionsort](https://github.com/furkancankay/SortExamples/assets/139324087/3e708671-5312-4f52-abf3-344eb0a29eb5)<br>
The notation is O(nlog(n))

## Merge Sort
This algorithm consists of two stages: the first stage is fragmentation and the second stage is merging. First, we reduce the list we have into one piece with a recursive function that divides it by 2. Then we look at the 2 data at first and combine them 1 by 1. Then 2, 2, then 4, 4, then 8, 8... until it's over.
<br>![image](https://github.com/furkancankay/SortExamples/assets/139324087/a51a12a1-7303-4da7-9c52-dbeb3f8851a9)<br>

The notation is O(nlog(n))

## 🥸 Requirement
`matplotlib` library version 3.8.0 to show them times


## A Few Screenshots
<br>![image](https://github.com/furkancankay/SortExamples/assets/139324087/f5084610-c584-42f5-b393-d3cd4ee6db0d)<br>
For example, in those examples we reached the result which is the best algorithm is insertion with the Large and Huge database.
<br>![image](https://github.com/furkancankay/SortExamples/assets/139324087/76aba83b-6d79-4ab2-bce4-3d2e300cdd88)<br>

And finally for small data, we can see that the merge algorithm is more logical than insertion.


## ⚠️ Warning

Cloning this repo makes you better developer. Be careful!
