# Euler method
from Euler_Method import EulerMethod
import matplotlib.pyplot as plt

if __name__ == '__main__':

    def equa_diff(x):
        return -1/tau * x + E/tau

    E = 6
    tau = 1

    result = EulerMethod.method1(equa_diff)
    temps = EulerMethod.temps()
    plt.plot(temps, result, "+r")
    plt.show()

