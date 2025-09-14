import math

def calculate_drag_constant(rho, A, Cd):
    """
    Calculate the drag constant based on fluid properties, object properties, and flow properties.
    
    Args:
    rho: float, density of fluid medium (kg/m^3)
    A: float, cross-sectional area of object (m^2)
    Cd: float, drag coefficient of object
    
    Returns:
    k: float, drag constant (kg/m)
    """
    k = 0.5 * rho * A * Cd
    return k


def projectile_motion_with_drag(v0, theta, m, rho, A, Cd, dt):
    """
    Calculate the trajectory of a projectile with drag.
    
    Args:
    v0: float, initial velocity (m/s)
    theta: float, launch angle (degrees)
    m: float, mass of projectile (kg)
    rho: float, density of fluid medium (kg/m^3)
    A: float, cross-sectional area of object (m^2)
    Cd: float, drag coefficient of object
    dt: float, time step (s)
    
    Returns:
    xs: list, horizontal position (m)
    ys: list, vertical position (m)
    vxs: list, horizontal velocity (m/s)
    vys: list, vertical velocity (m/s)
    """
    # calculate drag constant
    k = calculate_drag_constant(rho, A, Cd)

    # initial conditions
    v0x = v0 * math.cos(theta)
    v0y = v0 * math.sin(theta)
    x = 0
    y = 0
    vx = v0x
    vy = v0y

    # arrays to store the solutions
    xs = [x]
    ys = [y]
    vxs = [vx]
    vys = [vy]

    # loop through time steps
    while y >= 0:
        # calculate drag force and acceleration due to gravity
        fd = k * math.sqrt(vx**2 + vy**2) * vx
        fg = m * 9.81

        # calculate new velocities and positions
        vx = vx - fd/m * dt
        vy = vy - (fg + fd)/m * dt
        x = x + vx * dt
        y = y + vy * dt

        # store solutions
        xs.append(x)
        ys.append(y)
        vxs.append(vx)
        vys.append(vy)

    return xs, ys, vxs, vys


import matplotlib.pyplot as plt

# parameters
v0 = 50  # m/s
theta = 45  # degrees
m = 0.1  # kg
dt = 0.01  # s
a = 0.01  # cross section m^2
rho = 1.293  # kg/m^3
Cd = 0.47  # drag coefficient

# solve for projectile motion with drag
xs, ys, vxs, vys = projectile_motion_with_drag(v0, theta, m, rho, a, Cd, dt)

# plot results
plt.plot(xs, ys)
plt.title('Projectile Trajectory with Drag')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.show()
