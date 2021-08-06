import numpy as np

V = 5.0
a = 340
A1 = 0.05
L = 5.0

alpha = V /a**2

beta = A1 / L

print('alpha,beta=',alpha,beta)

psi_prime = 1.2 * 10**4
cap_psi_prime = 4.0 * 10**4

print(1/alpha/cap_psi_prime - beta*psi_prime)

print(beta/alpha*(1-psi_prime/cap_psi_prime))

