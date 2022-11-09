
class Point2D:

    def set(self, x=0, y=0):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def calculate_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5



point1 = Point2D()
point1.set()
print(point1.get())

point2 = Point2D()
point2.set(3, 4)
print(point2.get())

distance = point2.calculate_distance()

msg = f"The distance: {distance}" if distance != -1 else "Error"

print(msg)



