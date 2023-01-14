from Point import Point 


#
# Segment: 
# Label, left endpoint, right endpoint, slop, y-intercept, delta-x, delta-y
class Segment():
    Index = 0
    # SweepX = None
    def __init__(self, p1, p2):
        if (p1 < p2):
            self.left_endpoint = Point(p1[0], p1[1], 0) 
            self.right_endpoint = Point(p2[0], p2[1], 1) 
        else:
            self.left_endpoint = Point(p2[0], p2[1], 0) 
            self.right_endpoint = Point(p1[0], p1[1], 1) 
        
        self.xdiff = self.right_endpoint.x - self.left_endpoint.x
        self.ydiff = self.right_endpoint.y - self.left_endpoint.y
        
        self.slope = self.ydiff / self.xdiff 
        self.yintercept = self.left_endpoint.y - (self.slope * self.left_endpoint.x)

        self.label = Segment.Index 
        Segment.Index += 1

        self.SweepX = None

        # print(f'Segment {self.label}: L({self.left_endpoint.x},{self.left_endpoint.y}), R({self.right_endpoint.x},{self.right_endpoint.y}), m({self.slope}), b({self.yintercept})')
    
    def __str__(self):
        return "%s" % self.label

    def setSweepX(self, x):
        # print(f'[setSweepX] Seg: [{self.label}], orig: {self.SweepX}, new: {x}')
        self.SweepX = x 

    def heightAtSweep(self):
        # print(f'Current SweepX: {self.SweepX}')
        return (self.slope * self.SweepX) + self.yintercept

    # checks if given point lies inside the segment
    def interior(self, point):
        x = point.x 
        y = point.y 

        yprime = (self.slope * x) + self.yintercept

        if (y == yprime):
            if (point <= self.left_endpoint or point >= self.right_endpoint):
                return False
            return True 
        else: 
            return False

    
    def left(self):
        return self.left_endpoint
    
    def right(self):
        return self.right_endpoint
    

    def intersection(self, other):
        if (self.slope == other.slope): # parallel
            return None
        
        if (self.left_endpoint == other.left_endpoint or 
            self.left_endpoint == other.right_endpoint): 
            return self.left_endpoint
        
        if (self.right_endpoint == other.right_endpoint or 
            self.right_endpoint == other.left_endpoint): 
            return self.right_endpoint
        
        # print(f'Calculating Intersection Point')
        x = (other.yintercept - self.yintercept) / (self.slope - other.slope)
        y = (self.slope * x) + self.yintercept

        return Point(x, y, 2)