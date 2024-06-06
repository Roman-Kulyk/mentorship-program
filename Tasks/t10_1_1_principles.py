class Shape:
    def calculate_circle_area(self, radius):
        return 3.14 * (radius ** 2)
    
    def calculate_rectangle_area(self, length, width):
        return length * width
        
    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height
        
    def calculate_and_print_circle_area(self, radius):
        
        area = self.calculate_circle_area(radius) 
        print(f'The area of the circle is {area}')

    def calculate_and_print_rectangle_area(self, length, width):
        area = self.calculate_rectangle_area(length, width)
        print(f'The area of the rectangle is {area}')

    def calculate_and_print_triangle_area(self, base, height):
        area = self.calculate_triangle_area(base, height)
        print(f'The area of the triangle is {area}')



circle_1 = Shape()
print(circle_1.calculate_circle_area(5))
circle_1.calculate_and_print_circle_area(5)

triangle_1 = Shape()
print(triangle_1.calculate_triangle_area(3, 7))
triangle_1.calculate_and_print_triangle_area(3, 7)

rectangle_1 = Shape()
print(rectangle_1.calculate_rectangle_area(4, 6))
rectangle_1.calculate_and_print_rectangle_area(4, 6)