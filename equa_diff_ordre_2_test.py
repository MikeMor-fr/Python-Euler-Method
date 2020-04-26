# Euler method
from Euler_Method import EulerMethod
import matplotlib.pyplot as plt

if __name__ == '__main__':

    def f1(x, y, t):
        return -1/t * y + 1/t**2 * x + 2/t

    def f2(x, y, t):
    	return y

    u = EulerMethod.ordre2(f1, f2)[0]
    temps = EulerMethod.temps()

    plt.plot(temps, u, "+b")
    plt.show()