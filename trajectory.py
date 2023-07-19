from math import *
import matplotlib.pyplot as plt

def draw_trajectory(th, v):
    g = 9.8
    t_range = 2 * v * sin(radians(th)) / g
    t = 0
    x = []
    y = []
    

    while t <= t_range:
        vx = v * cos(radians(th)) * t
        vy = v * sin(radians(th)) * t -0.5 * 9.8 * t ** 2
        x.append(vx)
        y.append(vy)
        t += 0.0001
    
    plt.grid(True)
    plt.title("trajectory")
    plt.plot(x, y)
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.show()

if __name__ == '__main__':
    th = int(input("발사각(degree)를 입력해 주세요: "))
    v = int(input("발사속도(m/s)를 입력해 주세요: "))

    draw_trajectory(th, v)