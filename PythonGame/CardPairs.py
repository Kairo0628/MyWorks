import random

class FindPair:
  def __init__(self):
    self.Check = [False]
    while len(self.Check) != 16:
      self.Check.append(False)

    shape = ['♠', '♥', '♣', '♦️']
    nums = [1, 2, 3, 4]
    self.Board = []
    for i in shape:
      for j in nums:
        self.Board.append((i, j))
    random.shuffle(self.Board)

    self.TempBoard = ['XXXXXX']
    while len(self.TempBoard) != 16:
      self.TempBoard.append('XXXXXX')

    self.StartMessage()

  def StartMessage(self):
    print("게임 시작 !")

    print(self.Board[0:4])
    print(self.Board[4:8])
    print(self.Board[8:12])
    print(self.Board[12:16])

    print()
    print()

    print("규칙 : 행과 열의 번호를 입력하면 해당 칸을 뒤집습니다.")
    print("2행 3열칸을 뒤집고 싶다면 : '23' 입력")
    print("4행 1열칸을 뒤집고 싶다면 : '41' 입력")
    
    print()
    print()

    self.Play()

  def Play(self):
    self.count = 0

    while True:
      self.Show()

      self.Choose1 = int(input("열어볼 칸의 행과 열을 입력하세요 : "))
      row = str(self.Choose1)[0]
      col = str(self.Choose1)[1]
      pass

      if False not in self.Check:
        break

  def Equal(self):
    pass

  def Show(self):
    i = 0
    while i != 16:
      print(self.TempBoard[i:i+4])
      i = i + 4
    print()
          

FindPair()