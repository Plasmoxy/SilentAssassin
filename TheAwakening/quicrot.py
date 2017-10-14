from math import sin,cos,pi

rad = lambda a : a*pi/180
rot = lambda z, w, angle: (z-w)*( round( cos(rad(angle)), 7 ) + (1j)*round( sin(rad(angle)), 7) + w)

print(rot(1, 0, 90))