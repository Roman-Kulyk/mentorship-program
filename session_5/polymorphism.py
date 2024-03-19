class Polygon:
    def render(self):
        print('Rendering Polygon...')


class Square(Polygon):
    def render(self):
        print('Rendering Square...')


class Circle(Polygon):
    def render(self):
        print('Rendering Circle...')


s1 = Square()
s1.render()


c1 = Circle()
c1.render()


p1 = Polygon()
p1.render()