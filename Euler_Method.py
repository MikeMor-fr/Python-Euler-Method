# Euler method
from numpy import zeros

class EulerMethod():

	intervalle = eval(input('Intervalle d\'etude : '))
	N = int(input('Entrer le nombre de points : '))
	a = intervalle[0]
	b = intervalle[1]
	h = (b - a) / N

	@classmethod
	def temps(cls):
		T = [cls.a + i*cls.h for i in range(cls.N + 1)]
		return T


	@classmethod 
	def method(cls, function):
		X = zeros(cls.N + 1)
		X[0] = eval(input("Condition initiale X0 = "))
		for i in range(cls.N):
			X[i + 1] = X[i] + cls.h * function(X[i])
		return X

	@classmethod
	def ordre1(cls, function1, function2):
		X = zeros(cls.N + 1)
		Y = zeros(cls.N + 1)
		X[0] = eval(input("Condition initiale X0 = "))
		Y[0] = eval(input("Condition initiale Y0 = "))
		for i in range(cls.N):
			Y[i + 1] = Y[i] + cls.h * function1(X[i], Y[i])
			X[i + 1] = X[i] + cls.h * function2(X[i], Y[i])
		return (X, Y)

	@classmethod
	def ordre2(cls, function1, function2):
		X = zeros(cls.N + 1)
		Y = zeros(cls.N + 1)
		T = EulerMethod.temps()
		X[0] = eval(input("Condition initiale X0 = "))
		Y[0] = eval(input("Condition initiale Y0 = "))
		for i in range(cls.N):
			Y[i + 1] = Y[i] + cls.h * function1(X[i], Y[i], T[i])
			X[i + 1] = X[i] + cls.h * function2(X[i], Y[i], T[i])
		return (X, Y)
