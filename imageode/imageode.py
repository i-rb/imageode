def f(Y, t, a, b, c, d):
    y1, y2 = Y
    return [a*y1+b*y2, c*y1+d*y2]

def lodemap(a,b,c,d):
    y1 = np.linspace(-6.0, 6.0, 20)
    y2 = np.linspace(-6.0, 6.0, 20)
    Y1, Y2 = np.meshgrid(y1, y2)
    t = 0
    u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
    NI, NJ = Y1.shape

    for i in range(NI):
        for j in range(NJ):
            x = Y1[i, j]
            y = Y2[i, j]
            yprime = f([x, y], t, 1, 2, -2, 1)
            u[i,j] = yprime[0]
            v[i,j] = yprime[1]

    Q = plt.quiver(Y1, Y2, u, v, color='r')
    plt.axhline(y=0, color='k', linestyle='-.',linewidth=0.7)
    plt.axvline(x=0, color='k', linestyle='-.',linewidth=0.7)
    plt.xlabel('$y_1$')
    plt.ylabel('$y_2$')
    left, right = plt.xlim()
    up, down = plt.ylim()
    for y20 in [-0.5, 0.5, 1, -1, 1.5, -1.5]:
        tspan = np.linspace(0,5,100)
        y0 = [0.0, y20]
        ys = odeint(f, y0, tspan, (a, b, c, d))
        plt.plot(ys[:,0], ys[:,1], 'b-', linewidth=1) # path
    plt.xlim(left, right)  
    plt.ylim(up, down)
    plt.show()