from scipy.optimize import fsolve
import numpy as np
import sys

# Adapted from this tutorial/explanation: https://github.com/mrphlip/aoc/blob/master/2023/24.md
# because I never took matrix algebra and thus could not figure out the equations on my own

# But given everyone else in the AoC thread used some kind of solver, hey, I'm not alone
lines = [
    ((212542581053874, 357959731032403, 176793474286781 ),( -88, -256, -240)),
    ((154677220587564, 207254130208265, 139183938188421 ),( 184, 74, 235)),
    ((216869547613134, 38208083662943, 397740686492049 ),( 109, 262, -66)),
    ((221241619250961, 303902532813154, 249144641113790 ),( 48, 24, -112)),
    ((432610900189894, 347346225570463, 389169322099761 ),( -166, -99, -81))
]

#lines = []

#for line in sys.stdin:
#    coords,velocity = line.strip().split('@')
#    print(((coords),(velocity)))
#    lines.append(((coords),(velocity)))
#    x1,y1,z1 = coords.split(', ')
#    vx,vy,vz = velocity.split(', ')
#    x1 = int(x1)
#    y1 = int(y1)
#    y1 = int(z1)
#    vx = int(vx)
#    vy = int(vy)
#    vz = int(vz)
#    lines.append(((x1, y1, z1), (vx, vy, vz)))
#    lines.append((coords,velocity))

def equations(p):
    global lines
    x, y, z, xv, yv, zv = p
    res = []
    for i in lines[2:5]:
        ((x1,y1,z1),(xv1,yv1,zv1)) = i
#        x = x.astype(np.float)
#        y = y.astype(np.float)
#        z = z.astype(np.float)
#        xv = xv.astype(np.float)
#        yv = yv.astype(np.float)
#        zv = zv.astype(np.float)
        res.append((x-x1)*(yv-yv1) - (y-y1)*(xv-xv1))
        res.append((x-x1)*(zv-zv1) - (z-z1)*(xv-xv1))
    return res

x, y, z, xv, yv, zv = fsolve(equations, lines[0][0] + lines[0][1])

print(x)
print(y)
print(z)
