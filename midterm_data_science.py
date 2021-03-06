# -*- coding: utf-8 -*-
"""Midterm Data science.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C9Wljo7sSrk5IG2wgBQdaoT0thdyTE4b
"""

import math

"""Write a program by creating an 'Employee' class having the following functions and print the final salary.

Employee Class
"""

class Employee:
  def __init__(self, name, salary, hours, Year, addy):
    self.name = name
    self.salary = salary
    self.hours = hours
    self.Year = Year
    self.addy = addy

  def getInfo(self):
    print(self.salary)
  
  def Addsal(self):
    if self.salary < 500:
      self.salary = 10 + self.salary
      print(self.salary)
  
  def Addwork(self):
    thisHour = self.hours
    if thisHour > 7:
      self.salary = 5 + self.salary
      print(self.salary)
  
  def personInfocard(self):
    print(name,"\t",Year,"\t",addy)
    

    


salary = int(input('How much do you make?'))
hours = int(input('How many hours did you work?'))
name = (input('What is your name? '))
Year = int(input('What year did you join? '))
addy = input('what is your address ')
b = Employee("joe", salary, hours, Year, addy)
b.getInfo()
b.Addsal()
b.Addwork()
b.personInfocard()

"""Write a Shape class that has an empty initializer and a empty method for Area

Shape Class
"""

class Shape:
  def __init__():
    pass

  def area():
    pass

class Triangle(Shape):
  def __init__(self,L,W, Ang):
    self.L = L
    self.W = W
    self.Ang = Ang

  def area(self):
    tarea = ((self.L*self.W) * math.sin(self.Ang))/2
    print(tarea)

class Rectangle(Shape):
  def __init__(self, L, W):
    self.L = L
    self.W = W
  def area(self):
    rarea = (self.L * self.W)
    print(rarea)


c = Triangle(50, 60, 70)
c.area()

d = Rectangle(50, 60)
d.area()

"""Write a program by creating an ‘BigMatrixMath’ class having the following functions perform and add in large NumPy arrays 

Numpy Section
"""

import numpy as np
import random

class BigMatrixMath:
  def __init__(self):
    self.list = []
    pass
  
  def addMatrix(self, item = np.random.randint(-70,160, (40,40))):
    self.list.append(item)
    print(type(item))
  
  def printDimensions(self):
    count = 0
    for x in self.list:
      count+=1
      print("array", count, "size", x.shape)
    
  def dotProductEligble(self, a=np.array([]), b = np.array([])):
    if len(a) or len(b) == 0:
      print("dot product illeligable")
    else:
      try:
        np.dot(a,b)
        print("dot product elligble")
      except ValueError:
        print("dot prouct illeligble")

f = BigMatrixMath()
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1],[2],[3]])
f.addMatrix(a)
f.addMatrix(b)
f.addMatrix()
f.addMatrix()
f.addMatrix()
f.printDimensions()
f.dotProductEligble()

"""Create an array with values that are spaced linearly in a specified interval between 0.0 100.0 as a numpy.float64, over 25 values"""

import numpy as np
x = (np.arange(0.0,101.0,4.0))
print(x)

"""Given the following arrays show me a line where I can combine the values into a larger array:


"""

import numpy as np
a = np.array([[56,12], [39,74]])
b = np.array([[65,76]])
np.concatenate((a, b), axis=0)

"""Whats a command to reformat a singular dimension array of 12 elements into a 3, 4 matrix.


"""

import numpy as np
print(np.arange(12).reshape(3,4))