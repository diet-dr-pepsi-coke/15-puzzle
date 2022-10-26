import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog, QInputDialog, QErrorMessage
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint, choice

class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.qp = 0
        self.array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.position = 0
        self.mousex = 0
        self.mousey = 0
        self.row = 0
        self.col = 0
        self.zerox = 0
        self.zeroy = 0
        self.zerorow = 0
        self.zerocol = 0
        self.moves = 0
        self.line = 0
        self.linex = 0
        self.liney = 0
        self.place = 0
        self.one = ''
        self.two = ''
        self.three = ''
        self.four = ''
        self.five = ''
        self.six = ''
        self.setGeometry(75, 75, 700, 350)
        self.setWindowTitle('15-Puzzle')
        self.show()

    def configuration(self):
      self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      for i in range(len(self.array)):
          for j in range(len(self.array[i])):
              self.pick = choice(self.numbers)
              self.array[i][j] = self.pick
              self.numbers.remove(self.pick)
      array = self.array
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
      self.test()

    def test(self):
      count = 0
      for i in range(len(self.array)):
          for j in range(len(self.array)):
              count += 1
              if self.array[i][j] == 0:
                  self.position = count
      if self.total_inversions % 2 == 0:
          if 1 <= self.position <= 4 or 9 <= self.position <= 12:
              self.configuration()
          if 5 <= self.position <= 8 or 13 <= self.position <= 16:
              return self.array
      if self.total_inversions % 2 == 1:
          if 1 <= self.position <= 4 or 9 <= self.position <= 12:
              return self.array
          if 5 <= self.position <= 8 or 13 <= self.position <= 16:
              self.configuration()

    def mousePressEvent(self,event):
        self.mousex = event.x()
        self.mousey = event.y()
        self.findCell()
        self.findZero()
        if self.array == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
            self.change()
            return
        if self.zerorow == self.row or self.zerocol == self.col:
            while self.zerorow != self.row:
                if self.row - self.zerorow < 0:
                    self. array[self.zerorow][self.zerocol],self.array[self.zerorow - 1][self.zerocol] = self.array[self.zerorow - 1][self.zerocol],self.array[self.zerorow][self.zerocol]
                    self.zerorow -=1
                    self.moves += 1
                elif self.row - self.zerorow > 0:
                    self. array[self.zerorow][self.zerocol],self.array[self.zerorow + 1][self.zerocol] = self.array[self.zerorow + 1][self.zerocol],self.array[self.zerorow][self.zerocol]
                    self.zerorow += 1
                    self.moves += 1
            while self.zerocol != self.col:
                if self.col - self.zerocol < 0:
                    self. array[self.zerorow][self.zerocol],self.array[self.zerorow][self.zerocol - 1] = self.array[self.zerorow][self.zerocol - 1],self.array[self.zerorow][self.zerocol]
                    self.zerocol -= 1
                    self.moves += 1
                elif self.col - self.zerocol > 0:
                    self. array[self.zerorow][self.zerocol],self.array[self.zerorow][self.zerocol + 1] = self.array[self.zerorow][self.zerocol + 1],self.array[self.zerorow][self.zerocol]
                    self.zerocol += 1
                    self.moves += 1
        self.update()

    def paintEvent(self,event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.drawText(350,50,self.one)
        self.qp.drawText(350,75,self.two)
        self.qp.drawText(350,100,self.three)
        self.qp.drawText(350,125,self.four)
        self.qp.drawText(350,150,self.five)
        self.qp.drawText(350,175,self.six)
        self.x = 50
        self.y = 50
        i = 0
        for x in range(4):
            self.drawSquare(number = self.array[0][i])
            i += 1
            self.x += 50
        self.x = 50
        self.y = 100
        j = 0
        for x in range(4):
            self.drawSquare(number = self.array[1][j])
            j += 1
            self.x += 50
        self.x = 50
        self.y = 150
        k = 0
        for x in range(4):
            self.drawSquare(number = self.array[2][k])
            k += 1
            self.x += 50
        self.x = 50
        self.y = 200
        l = 0
        for x in range(4):
            self.drawSquare(number = self.array[3][l])
            l += 1
            self.x += 50
        self.qp.drawText(50,300, 'Moves: ' + str(self.moves))
        if self.array == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
            winpen = QPen(QColor(Qt.red))
            self.qp.setPen(winpen)
            self.qp.setFont(QFont('arial',50))
            self.qp.drawText(50,150,'WINNER!')
        self.qp.end()


    def drawSquare(self, number):
        pen = QPen(QColor(Qt.black))
        self.qp.setPen(pen)
        self.qp.drawRect(self.x, self.y, 50, 50)
        if number != 0:
            self.qp.drawText(self.x + 20, self.y + 30, str(number))
        if number == 0:
            self.zerox = self.x
            self.zeroy = self.y

    def findCell(self):
        for x in range(50,250):
            for y in range(50,250):
                if x == self.mousex and y == self.mousey:
                    self.col = x//50 - 1
                    self.row = y//50 - 1

    def findZero(self):
        for x in range(50,250):
            for y in range(250):
                if x == self.zerox and y == self.zeroy:
                    self.zerocol = x//50 - 1
                    self.zerorow = y//50 - 1

    def change(self):
        name = QInputDialog.getText(self, 'High Score!', 'Please Enter name for leaderboards:')

    def leaderboard(self, file):
        self.one = my_file.readline()
        self.two = my_file.readline()
        self.three = my_file.readline()
        self.four = my_file.readline()
        self.five = my_file.readline()
        self.six = my_file.readline()


if __name__ == '__main__':
  my_file = open('leaderboard.txt','r+')
  app = QApplication(sys.argv)
  ex = Test()
  ex.configuration()
  ex.leaderboard(my_file)
  sys.exit(app.exec_())
