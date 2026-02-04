class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        y = 0
        x = 0

    def afficherX_afficherY(self):
        return f"horizontal: {self.x},verticale: {self.y}"

    def changerX_changerY(self):
        self.x = 30
        self.y = 40
        return f"horizontal: {self.x},verticale: {self.y}"
x = 10
y = 2
point = Point(x,y)
print(point.afficherX_afficherY())
print(point.changerX_changerY())