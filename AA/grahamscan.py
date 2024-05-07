import math

def polar_angle(point):
    x1, y1 = point
    angle = math.atan2(y1, x1)  
    return math.degrees(angle)

def turn_calculator(prev, curr, next):
    x1, y1 = prev
    x2, y2 = curr
    x3, y3 = next
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    
    '''If cross product is +ve : left turn
       If cross product is -ve : right turn
       If cross product is 0 : collinear
    '''
    return cross_product

def graham_scan(points):
    if len(points) < 3:
        return []

    # Sort the points based on their polar angle
    sorted_points = sorted(points, key=polar_angle)

    # Initialize the stack with the first two points
    # Always part of the convex hull
    stack = [sorted_points[0], sorted_points[1]]

    for i in range(2, len(sorted_points)):
        while len(stack) > 1 and turn_calculator(stack[-2], stack[-1], sorted_points[i]) <= 0:
            stack.pop()  
        stack.append(sorted_points[i])

    return stack

input_points = [(0, 3), (1, 1), (2, 2), (4, 4),(0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(input_points)
convex_hull = sorted(convex_hull,key=polar_angle)
print("Convex Hull:", convex_hull)
