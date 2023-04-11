# importing all necessary modules
from tkinter import *
from tkinter import ttk
import numpy as np
import time


def show(n: int, data: list, colours: list):

    # n is length of the array data
    # data is the array itself
    # colours is an array of colors
    canvas.delete('all')

    width = 1560/(3*n-1)   # width variable is the width of each bar
    gap = width/2          # gap is the spacing between the bars

    for i in range(n):

        # this function will display an array of "bar"
        canvas.create_rectangle(7+i*width+i*gap, 0, 7 +(i+1)*width+i*gap, data[i],fill=colours[i])
            #The create_rectangle method takes 4 coordinates: 
            #canvas. create_rectangle(x1, y1, x2, y2, **kwargs)
            #- with (x1,y1) the coordinates of the top left corner and (x2, y2) those of the bottom right corner.
    
    
    # this function will help us to see every step of the sorting algorithm
    # the purpose of this function is to update the screen in runtime
    win.update_idletasks()


def shuffle():
    np.random.shuffle(arr)
    show(N, arr, color)


def mergesort(arr, left, right):
 if left < right:
  m = (left+right)//2
  mergesort(arr, left, m)
  mergesort(arr, m+1, right)

  j = m+1
  if arr[m] <= arr[m+1]:
   return

  while left <= m and j <= right:
   show(N, arr, ['blue' if x == left or x ==j else 'grey' for x in range(N)])
   time.sleep(1/speed)
   if arr[left] <= arr[j]:
        left += 1
   else:
    show(N, arr, ['red' if x == left or x ==j else 'grey' for x in range(N)])
    
    # array of colours where only the focused bars
    # are displayed red since left >arr[j]
    time.sleep(1/speed)
    temp = arr[j]
    
    # storing the smaller element in temp variable
    i = j
    while i != left:
        arr[i] = arr[i-1]
        show(N, arr, ['red' if x == i or x ==j else 'grey' for x in range(N)])
        time.sleep(1/speed)
        i -= 1
    
    # this while loop will shift all the elements one step to right to make the place empty for the temp variable
    # upon reaching the desired location i.e. left, the temp value will be inserted into that location.
    # this process is much like insertion sort
    arr[left] = temp

    show(N, arr, ['green' if x == left or x ==j else 'grey' for x in range(N)])
    time.sleep(1/speed)
    left += 1
    m += 1
    j += 1

# this function call the mergesort function which will
# start the animation.
def start():
    mergesort(arr, 0, N-1)
    show(N, arr, ['green' for _ in range(N)])



win = Tk()
N = 50 # length of the array
speed = 100 # how fast the array will be sorted

# creating the array using linspace function from numpy
arr = np.linspace(10, 390, N, dtype=np.uint16)
color = ['grey' for _ in range(N)]

ttk.Label(win, text='Merge Sort visualizer').pack()
canvas = Canvas(win, width=800, height=400, bg='white')
canvas.pack()

ttk.Button(win, text='Start sorting', command=start).pack(side='right', padx=5, pady=5)
ttk.Button(win, text='Shuffle array', command=shuffle).pack(side='right')

shuffle()
show(N, arr, color)

win.mainloop()
