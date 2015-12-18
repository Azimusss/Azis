import math

class Vector:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def get_len(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def len(self):
        return self.get_len()

    def as_point(self):
        return self.x, self.y

    def rotate(self, angle):
        angle = math.radians(angle)
        x1 = self.x * math.cos(angle) - self.y * math.sin(angle)
        y1 = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector((x1, y1))

    def __add__(self, other):
        xs = self.x + other.x
        ys = self.y + other.y
        return Vector((xs, ys))

    def __mul__(self, other):
        m1 = other * self.x
        m2 = other * self.y
        return Vector((m1, m2))

    def __sub__(self, other):
        xs = self.x - other.x
        ys = self.y - other.y
        return Vector((xs, ys))

    def __repr__(self):
        return "v (%s, %s)" % (self.x, self.y)

    def normalize(self):
        x = self.x / self.get_len()
        y = self.y / self.get_len()
        return Vector((x, y))

if __name__ == "__main__":
    v1 = Vector((10, 10))
    print(v1)

    v1 = v1.rotate(45)

    print(v1)
