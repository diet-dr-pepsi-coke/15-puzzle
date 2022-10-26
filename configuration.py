from random import choice
from math import ceil

class Test(object):

    def __init__(self):
      self.array = [[0, 0, 0,0], [0, 0, 0, 0], [0, 0, 0,0], [0, 0, 0, 0]]


    def configuration(self):
      self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      for i in range(len(self.array)):
          for j in range(len(self.array[i])):
              self.pick = choice(self.numbers)
              self.array[i][j] = self.pick
              self.numbers.remove(self.pick)
      array = self.array
      print(self.array) #made random array
      self.arraylist = list()
      inversion_per_number = list()
      for i in range(len(self.array)):
          for j in range(len(self.array[i])):
              self.arraylist.append(self.array[i][j]) #put random array into list form
              current = self.array[i][j]
              not_inversions = 0
              inversions = 0
              if 0 not in self.arraylist:
                  inversions -= 1
              for x in self.arraylist:
                  if current > x:
                      not_inversions += 1
              if current - not_inversions > 0:
                  inversion_per_number.append(current + inversions - not_inversions)
              else:
                  inversion_per_number.append(0)
      self.total_inversions = 0
      for i in range(len(inversion_per_number)):
          self.total_inversions += inversion_per_number[i]
      print(self.total_inversions) #found total number of inversions
      self.test()

    def test(self):
      count = 0
      for i in range(len(self.array)):
          for j in range(len(self.array)):
              count += 1
              if self.array[i][j] == 0:
                  position = count
      if self.total_inversions % 2 == 0:
          if 1 <= position <= 4 or 9 <= position <= 12:
              self.configuration()
          if 5 <= position <= 8 or 13 <= position <= 16:
              return
      if self.total_inversions % 2 == 1:
          if 1 <= position <= 4 or 9 <= position <= 12:
              return
          if 5 <= position <= 8 or 13 <= position <= 16:
              self.configuration()


ok = Test()
Test.configuration(ok)
##for mouse eventt
    if 50 < event.x() < 250 or 50 < event.y() < 250:
        if (event.x() > 25 + self.zerox and event.y() > 25 + self.zeroy):
            return
        if (event.x() > 25 + self.zerox and event.y() < self.zeroy - 25):
            return
        if (event.x() < self.zerox - 25 and event.y() > 25 + self.zeroy):
            return
        if (event.x() < self.zerox - 25 and event.y() < self.zeroy - 25):
            return
        else:
            print(event.x(),event.y())
