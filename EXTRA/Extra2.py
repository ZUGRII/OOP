##
#
class Ace():
    def __init__(self):
        self.hp = 100
        self.name = "Sam"

    def __str__(self):
        return  "hp = {} \nname = {}".format(self.hp,self.name)

    def __repr__(self):
        output = "Ace : hp= {} \nname = {}".format(self.hp,self.name)
        return output

obj = Ace()
#print(obj)
obj # works in shell