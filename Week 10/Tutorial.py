#.......
class Rectangle():
    def __init__(self, length, width):

        if(length < 0 or width < 0):
            print("Error, no negative numbers")
            return
        else:
            self.r_length = length
            self.r_width = width

    def calculate_area(self):
        self.area = self.r_width * self.r_length
        return self.area

    def calculate_perimeter(self):
        self.perimeter = (2 * self.r_width) + (2 * self.r_length)
        return self.perimeter



rect1 = Rectangle(8,2)
print(rect1.calculate_area)