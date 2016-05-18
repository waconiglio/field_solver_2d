import numpy as np
import math
import cmath
import png

xsize = 64
ysize = 64

mu0 = 1.0

def bfield_cyl(Iz, x0, y0, x, y):
  # compute R,theta first, then make rectangular
  r = max(math.sqrt((x-x0)**2 + (y-y0)**2),0.5)
  theta = math.atan2(y-y0,x-x0)
  R = mu0*Iz/2/math.pi/r

  Bx = -R*math.sin(theta)
  By = R*math.cos(theta)

  return (Bx,By)


Bx = np.ndarray( (xsize,ysize) , dtype=float)
By = np.ndarray( (xsize,ysize) , dtype=float)

for i in range(xsize):
  for j in range(ysize):
    B = bfield_cyl(1.0,24.0,24.0,i,j)
    Bx[i,j] = B[0]
    By[i,j] = B[1]

a = np.ndarray((xsize,ysize), dtype=np.uint8)
for i in range(xsize):
  for j in range(ysize):
    a[i,j] = min(max(255+25*math.log(math.sqrt(Bx[i,j]**2 + By[i,j]**2)), 0),255)

png.from_array(a, mode='L').save('output.png')
