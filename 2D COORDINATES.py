class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) :
        return f" {self.x} , {self.y}"
    def euclidean_distance(self,other):
         return ((self.x-other.x )**2 + (self.y-other.y)**2)**0.5
    def distance_from_origin(self):
      return self.euclidean_distance(Point(0, 0))
class Line:
    def __init__(self,A,B,C):
        self.a=A
        self.b=B
        self.c=C
    def __str__(self):
        return f" {self.a}X + {self.b}Y+ {self.c} =0"
    def distance(self,other):
        if self.a*other.x+self.b*other.y+self.c==0:
            return "lies on thye line"
        else: 
            return " does not lie on the line"
    def shortest_distance(self,point):
      return abs (self.a*point.x+self.b*point.y+self.c)/(self.a**2+self.b**2)


        

    
# p1=Point(0,0)
# p2=Point(1,1)
# print(p1)
# print(p1.euclidean_distance(p2))
# print(p1.distance_from_origin())
# l1=Line(3,4,5)
l1=Line(1,1,-2)
l2=Point(1,1)
print(l1)
print(l2)
print(l1.distance(l2))
print(l1.shortest_distance(l2))
