class Circle: # did everything except printing the circle. Dont know how to draw in terminal:)
    def __init__(self,radius):
        self.radius = radius
    def calc_area(self):
        area = self.radius ** 2 * 3.1415926535 # Pi number
        return area
    def __add__(self, other):
        radius_add = self.radius + other.radius
        return radius_add
    def __gt__(self, other):
        compare = self.radius > other.radius
        return compare
    def __eq__(self, other):
        equal = self.radius == other.radius
        return equal
    def __repr__(self):
        return f'Circle with radius {self.radius}'
    

my_circle = Circle(5)

my_circle_2 = Circle(7)

circles_list = [my_circle, my_circle_2]

#Testing
print(my_circle.calc_area())
print(my_circle + my_circle_2)
print(my_circle < my_circle_2)
print(my_circle == my_circle_2)
circles_list.sort(key = lambda x: x.radius, reverse = True)
print(circles_list)