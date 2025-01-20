# Hi! This file contains the Shape class which calculates and print areas
# This class doesn't match to OOP principles. You need to fix this code

class Shape:
    def calculate_circle_area(self,radius):
        return 3.14 * (radius ** 2)
    
    def calculate_rectangle_area(self, length, width):
        return length * width
    
    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height
    
    def print_circle_area(self,radius):
        area = 3.14 * (radius ** 2)
        print(f'The area of the circle is {area}')

    def print_rectangle_area(self, length, width):
        area = length * width
        print(f'The area of the rectangle is {area}')
    
    def print_triangle_area(self, base, height):
        area = 0.5 * base * height
        print(f'The area of the triangle is {area}')

    def calculate_and_print_area(self, shape, dimensions): # DRY
        if shape == 'circle':                              
            radius = dimensions[0]  # KISS
            area = 3.14 *(radius **2) 
            print(f'The area of the circle is {area}')
        elif shape == 'rectangle':
            length, width = dimensions  # KISS
            area = length * width
            print(f'The area of the rectangle is {area}')
        elif shape == 'triangle':
            base, height = dimensions  # KISS
            area = 0.5 * base * height
            print(f'The area of the triangle is {area}')
        else:
            print('Invalid shape')

    def some_unused_method(self): # YAGNI
        pass

shape = Shape()
shape.print_circle_area(5)
shape.print_rectangle_area(4, 6)
shape.calculate_triangle_area(3, 7)
shape.calculate_and_print_area('circle', [5])
shape.calculate_and_print_area('rectangle', [4, 6])
shape.calculate_and_print_area('triangle', [3, 7])
shape.calculate_and_print_area('pentagon', [3, 7])