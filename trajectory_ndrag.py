import numpy as np
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import ttk

def trajectory(h, v, alpha):
    """Calculate the trajectory of a projectile.

    Parameters
    ----------
    h : float
        Initial height of the projectile.
    v : float
        Initial velocity of the projectile.
    alpha : float
        Initial angle of the projectile.

    Returns
    -------
    x : list
        List of x coordinates of the trajectory.
    y : list
        List of y coordinates of the trajectory.
    """
    # vars
    vx = v * math.cos(math.radians(alpha))
    vy = v * math.sin(math.radians(alpha))
    g = 9.81

    # time of flight
    tof = (v * math.sin(math.radians(alpha)) + math.sqrt(v ** 2 * math.sin(math.radians(alpha)) ** 2 + 2 * g * h)) / g
    #print(tof)

    # x and y coordinates
    x = [vx * t for t in np.linspace(0, tof, 100)]
    y = [h + vy * t - 0.5 * g * t ** 2 for t in np.linspace(0, tof, 100)]

    return x, y

# create window
window = tk.Tk()
window.title('Trajectory')

# create labels
label1 = ttk.Label(window, text='Initial height: ')
label2 = ttk.Label(window, text='Initial velocity: ')
label3 = ttk.Label(window, text='Initial angle: ')

# create entry boxes
entry1 = ttk.Entry(window)
entry2 = ttk.Entry(window)
entry3 = ttk.Entry(window)

# create button
button = ttk.Button(window, text='Plot')

# create function
def plot():
    x = trajectory(float(entry1.get()), float(entry2.get()), float(entry3.get()))[0]
    y = trajectory(float(entry1.get()), float(entry2.get()), float(entry3.get()))[1]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.rcParams["figure.autolayout"] = True
    plt.title('Trajectory')
    #plt.show()
    # now I need to make a new plot with the x values as time and the y values as height
    tof = (float(entry2.get()) * math.sin(math.radians(float(entry3.get()))) + math.sqrt(float(entry2.get()) ** 2 * math.sin(math.radians(float(entry3.get()))) ** 2 + 2 * 9.81 * float(entry1.get()))) / 9.81
    x = np.linspace(0, tof, 100)
    y = [float(entry1.get()) + float(entry2.get()) * math.sin(math.radians(float(entry3.get()))) * t - 0.5 * 9.81 * t ** 2 for t in x]
    # draw it on a subplot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='time (s)', ylabel='height (m)', title='Height vs. Time')
    ax.grid()
    plt.show()



# bind button to function
button.config(command=plot)

# pack labels and entry boxes
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()

# pack button
button.pack()

# run window
window.mainloop()


