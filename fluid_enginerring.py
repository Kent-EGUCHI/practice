import numpy as np
a = 340
As = np.pi * 10**(-4)
L = 2.5 * 10**(-2)
V = 5.0 * 10**(-4)
f = a/2/np.pi*np.sqrt(As/V/L)

# a = 340
# As = 12.56 * 10**(-4)
# L = 4 * 10**(-2)
# V = 846.76 * 10**(-6)
# f = a/2/np.pi*np.sqrt(As/V/L)
print(f)