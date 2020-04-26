# Euler method
import matplotlib.pyplot as plt
from Euler_Method import EulerMethod as EM

g = 9.81

def f1(x, y):
	return g - 1/28 * y**2

def f2(x, y):
	return y

if __name__ == '__main__':

	distance = EM.ordre1(f1, f2)[0]
	vitesse = EM.ordre1(f1, f2)[1]
	temps = EM.temps()

	plt.plot(temps, distance, "*b")
	plt.show()
	plt.plot(temps, vitesse, "+r")
	plt.show()
