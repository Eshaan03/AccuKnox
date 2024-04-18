class Rectangle:
    def __init__(self, length, breadth):

        if not (isinstance(length, int) or isinstance(breadth, int)):
            raise TypeError("The values should be integer!")
        else:
            self.length = length
            self.breadth = breadth

rect_1 = Rectangle("10","20")
rect_2 = Rectangle(20,30)

rectangles = [rect_1, rect_2]

for rect in rectangles:
    print(f"The length of the rectangle is {rect.length} and the breadth is {rect.breadth}")

