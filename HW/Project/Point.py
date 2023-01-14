
# Point class, ordered by x-coordinate

class Point():
    def __init__(self, x, y, ptype):
        self.x = x  
        self.y = y 
        self.ptype = ptype # 0 for starting point, 1 for end point, 2 for intersection point
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def compare(self, other):
        if (self is other): 
            return 0
        
        xdiff = self.x - other.x 
        if (xdiff > 0): 
            return 1 
        if (xdiff < 0): 
            return -1

        # else: xdiff == 0 
        ydiff = self.y - other.y 
        if (ydiff > 0): 
            return 1 
        if (ydiff < 0): 
            return -1

        # same x and y coordinares
        return 0 

    def __lt__(self, other):
        return self.compare(other) < 0
    def __le__(self, other):
        return self.compare(other) <= 0
    def __gt__(self, other):
        return self.compare(other) > 0
    def __ge__(self, other):
        return self.compare(other) >= 0
    def __eq__(self, other):
        if (other is None):
            return False 
        return self.compare(other) == 0
    



