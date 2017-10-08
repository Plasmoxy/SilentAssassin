# Simple complex point rotation
# by Plasmoxy

# INPUT :
# First line - x and y of point you want to rotate, separated by spaces
# Second line - x and y of the center of rotation
# Third line - angle by which you want to rotate the point around center

# based on complex multiplication rotation
# z' = (z-w) ( cos(theta) + isin(theta) ) + w

# positive angles to rotate counter-clockwise
# negative angles to rotate clockwise

from math import sin,cos,pi

point=[]
center=[]

try:
    point_input = input("Point: ").split(" ")
    center_input = input("Center: ").split(" ")
    angle_deg = float(input("Angle (degrees):"))
    for i in point_input: # yeah this could be done much simpler but whatever xD
            point.append(float(i))
    for i in center_input:
            center.append(float(i))
    
    if len(point) != 2 or len(center) != 2:
        raise Exception("Need two numbers for each point separated by spaces !")
except ValueError as e:
    print("Enter only numbers !")
    exit(-1)
except Exception as e:
    print("\nError in input:")
    print(e)
    exit(-1)

angle = angle_deg*(pi/180)

print("\nSTARTING POINT :", point)
print("ROTATING AROUND:", center)
print("ANGLE OF ROTATION:", angle_deg, "degrees")

point_c = complex(point[0], point[1])
center_c = complex(center[0], center[1])

rotpoint_c = (point_c - center_c) * ( cos(angle) + (1j)*sin(angle) ) + center_c

rotpoint = [round(rotpoint_c.real, 7), round(rotpoint_c.imag, 7)]

print("\nResult:", rotpoint, "\n")