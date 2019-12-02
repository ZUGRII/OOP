#


class Player():
	def __init__(self, hp = 100):
		self.__hp = hp # no other can change it
	def getHP(self):
		return self.__hp
	def setHP(self, damage):
		self.__hp -= damage

Players =[]
for i in range(1,6):
    correct = False
    while(correct == False):

        try:
            hp = int(input("Enter hp: "))
            player = Player(hp)
            Players.append(player)
            correct = True

        except(ValueError):
            print("Error 404")

for p in Players:
    print(p.getHP())
